import os
import re

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd
import datetime

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    user = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])
    user_cash = user[0]["cash"]

    user_summary = db.execute("SELECT company, symbol, sum(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY user_id, company, symbol HAVING total_shares > 0;", session["user_id"])
    user_summary = [dict(x, **{'current_price': lookup(x['symbol'])['price']}) for x in user_summary]
    user_summary = [dict(x, **{'total': x['current_price']*x['total_shares']}) for x in user_summary]

    grand_total = user_cash + sum([x['total'] for x in user_summary])

    return render_template("index.html", user_cash=user_cash, user_summary=user_summary, grand_total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    elif request.method == "POST":
        stock = lookup(request.form.get("symbol").upper())

        if stock == None:
            return apology("INVALID SYMBOL")

        share_price = float(stock["price"])
        shares = request.form.get("shares")

        if not shares.isdigit():
            return apology("Number of shares must be a positive digit!")

        total_price = share_price * float(shares)

        rows = db.execute("SELECT * FROM users WHERE id = ?;", session["user_id"])
        user_cash = rows[0]["cash"]

        if user_cash < total_price:
            return apology("NOT ENOUGH MONEY")


        db.execute("INSERT INTO transactions(user_id, timestamp, company, symbol, shares, price, transaction_type) VALUES(?, ?, ?, ?, ?, ?, ?);",
                   session["user_id"], datetime.datetime.now(), stock["name"], stock["symbol"], shares, share_price, "BUY ORDER")


        db.execute("UPDATE users SET cash = ? WHERE id = ?;",
                   (user_cash - total_price), session["user_id"])

        return redirect("/")




@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM transactions WHERE user_id = ?;", session["user_id"])
    return render_template("history.html", transactions=transactions)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        quotes = lookup(request.form.get("symbol").upper())

        if quotes == None:
            return apology("INVALID SMBOL")

        quotes["price"] = usd(quotes["price"])

        return render_template("quoted.html", quotes=quotes)



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")

    elif request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        previous_username = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        if len(previous_username) > 0:
            return apology("Username already taken", 400)

        # Ensure password & confirmation was submitted
        if not request.form.get("password"):
            return apology("must provide password", 400)
        if not request.form.get("confirmation") or request.form.get("confirmation") != request.form.get("password"):
            return apology("must provide password", 400)
        if len(request.form.get("password")) < 8:
            return apology("Password must be at least 8 characters long!", 400)
        if (
            not re.search("[a-zA-Z]", request.form.get("password"))
            or not re.search("[0-9]", request.form.get("password"))
            or not re.search("[!@#$%^&*()]", request.form.get("password"))
        ):
            return apology("Password must contain characters, digits and symbols!", 400)

        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("confirmation"))

        db.execute("INSERT INTO users (username, hash) VALUES(?)", (username, hash))

        return render_template("login.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_stocks = db.execute("SELECT symbol, sum(shares) as total_shares FROM transactions WHERE user_id = ? GROUP BY user_id, symbol HAVING total_shares > 0;", session["user_id"])

    if request.method == "GET":
        return render_template("sell.html", user_stocks=user_stocks)

    if request.method == "POST":
        selected_symbol = request.form.get("symbol")
        selected_shares = int(request.form.get("shares"))

        symbols_ref = {d['symbol']: d['total_shares'] for d in user_stocks}

        if selected_symbol in symbols_ref:

            if selected_shares > symbols_ref[selected_symbol]:
                return apology("YOU DONT HAVE THAT MANY SHARES")

            query = lookup(selected_symbol)

            user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

            db.execute("INSERT INTO transactions(user_id, timestamp, company, symbol, shares, price, transaction_type) VALUES(?, ?, ?, ?, ?, ?, ?);",
                    session["user_id"], datetime.datetime.now(), query["name"], selected_symbol, -selected_shares, query["price"], "SELL ORDER")


            db.execute("UPDATE users SET cash = ? WHERE id = ?;",
                    (user[0]['cash'] + (query['price'] * selected_shares)), session["user_id"])

            flash("Sold!")

            return redirect("/")
