## Flask
- 3rd party library/framework used to create/run your own web server
- You need to have at least an ```app.py``` file and a ```templates/``` directory for your html
- Use **Jinja** on html side to connect the python and html
app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
	return render_template("index.html")
```

index.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>hello</title>
	</head>
	<body>
		hello, world
	</body>
</html>
```

- In order to pass values via the URL:
app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
	if "name" in request.args:
		name = request.args["name"]
	else:
		name = "world"
	return render_template("index.html", name=name)
```

index.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>hello</title>
	</head>
	<body>
		hello, {{ name }}
	</body>
</html>
```

therefore page will print hello, Jim if URL looks like: ```
localhost:3000/?name=Jim```

A better app.py:
```
from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
	name = request.args.get("name", "world")
	return render_template("index.html", name=name)
```
## Forms
app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/greet")
def greet():
	return render_template("greet.html", name=request.args.get("name", "world"))
```

templates/index.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>hello</title>
	</head>
	<body>
		<form action="/greet" method="get">
			<input name="name" type="text" placeholder="Name">
			<button type="submit">Greet</button>
		</form>
	</body>
</html>
```

templates/greet.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>hello</title>
	</head>
	<body>
		hello, {{ name }}
	</body>
</html>
```

## Layouts
- If you have repeating pages of html that are almost identical you can use layouts

layout.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>hello</title>
	</head>
	<body>
		{% block body %}{% endblock %}
	</body>
</html>
```

- Now you can plug the all the contents of a file in the body

index.html
```
{% extends "layout.html" %}

{% block body %}

	<form action="/greet" method="get">
		<input name="name" type="text" placeholder="Name">
		<button type="submit">Greet</button>
	</form>

{% endblock %}
```

greet.html
```
{% extends "layout.html" %}

{% block body %}

	hello, {{ name }}

{% endblock %}
```

## Request Methods
- When you are sending something over the internet you want to use ```POST``` so the data does not show up in the URL

index.html
```
{% extends "layout.html" %}

{% block body %}

	<form action="/greet" method="post">
		<input name="name" type="text" placeholder="Name">
		<button type="submit">Greet</button>
	</form>

{% endblock %}
```

app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
	return render_template("index.html")


@app.route("/greet", methods=["POST"])
def greet():
	return render_template("greet.html", name=request.args.get("name", "world"))
```

Combining similar routes

index.html
```
{% extends "layout.html" %}

{% block body %}

	<form action="/" method="post">
		<input name="name" type="text" placeholder="Name">
		<button type="submit">Greet</button>
	</form>

{% endblock %}
```

app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET, POST"])
def index():
	if request.method == "GET":
		return render_template("index.html")
	elif request.method == "POST":
		return render_template("greet.html", name=request.form.get("name", "world"))
```

When trying to access submission arguments you use ```request.form``` instead of ```request.args```

## Frosh IMs

app.py
```
from flask import Flask, render_template, request

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = ["Basketball", "Soccer", "Volleyball"]

@app.route("/")
def index():
	return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	if not name:
		return render_template("failure.html")
		
	sport = request.form.get("sport")
	if sport not in SPORTS:
		return render_template("failure.html")
		
	REGISTRANTS[name] = sport
	return render_template("success.html")


@app.route("/registrants")
def registrants():
	return render_template("registrants.html", registrants=REGISTRANTS)
```

templates/layout.html
```
<!DOCTYPE html>

<html lang="en">
	<head>
		<meta name="viewport" content="initial-scale=1, width=device-width"
		<title>froshims</title>
	</head>
	<body>
		{% block body %}{% endblock %}
	</body>
</html>
```

templates/index.html
```
{% extends "layout.html" %}
{% block body %}
	<form action="/register" method="post">
		<input autocomplete="off" autofocus required name="name" placeholder="Name" type="text">
		<select name="sport">
			<option disabled selected>Sport</option>
			{% for sport in sports %}
				<option value="{{ sport }}">{{ sport }}</option>
			{% endfor %}
		</select>
		<button type="submit">Register</button>
	</form>
{% endblock %}
```

templates/success.html
```
{% extends "layout.html" %}
{% block body %}
	You are registered!
{% endblock %}
```

templates/registrants.html
```
{% extends "layout.html" %}
{% block body %}
	<ul>
		{% for name in registrants %}
			<li>{{ name }} is registered for {{ registrants[name] }}</li>
		{% endfor %}
	</ul>
{% endblock %}
```

templates/failure.html
```
{% extends "layout.html" %}
{% block body %}
	You are not registered!
{% endblock %}
```

## SQLite & Python
- Using a database

app,py
```
from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = ["Basketball", "Soccer", "Volleyball"]

@app.route("/")
def index():
	return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
	name = request.form.get("name")
	sport = request.form.get("sport")
	if not name or sport not in SPORTS:
		return render_template("failure.html")

	db.execute("INSERT INTO registrants (name, sport) VALUES(?, ?)", name, sport)
		
	return redirect("/registrants")


@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM registrants WHERE id = ?", id)
    return redirect("/registrants")

@app.route("/registrants")
def registrants():
	registrants = db.execute("SELECT * FROM registrants*")
	return render_template("registrants.html", registrants=REGISTRANTS)
```

templates/registrants.html
```
  {% extends "layout.html" %}

  {% block body %}
      <h1>Registrants</h1>
      <table>
          <thead>
              <tr>
                  <th>Name</th>
                  <th>Sport</th>
                  <th></th>
              </tr>
          </thead>
          <tbody>
              {% for registrant in registrants %}
                  <tr>
                      <td>{{ registrant.name }}</td>
                      <td>{{ registrant.sport }}</td>
                      <td>
						<form action="/deregister" method="post">
							<input name="id" type="hidden" value="{{ registrant.id }}">
							<input type="submit" value="Deregister">
						</form>
					  </td>
                  </tr>
              {% endfor %}
          </tbody>
      </table>
  {% endblock %}
```

## Cookies & Sessions
- **Cookies** - allows the website to remember your login after the user logs in once

app.py
```
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")
```

templates/layout.html
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>store</title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```

templates/index.html
```
{% extends "layout.html" %}

{% block body %}

    {% if session["name"] %}
        You are logged in as {{ session["name"] }}. <a href="/logout">Log out</a>.
    {% else %}
        You are not logged in. <a href="/login">Log in</a>.
    {% endif %}

{% endblock %}
```

templates/login.html
```
{% extends "layout.html" %}

{% block body %}

    <form action="/login" method="post">
        <input autocomplete="off" autofocus name="name" placeholder="Name" type="text">
        <button type="submit">Log In</button>
    </form>

{% endblock %}
```

## Shopping Cart

app.py
```
from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)

# Connect to database
db = SQL("sqlite:///store.db")

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route("/")
def index():
    books = db.execute("SELECT * FROM books")
    return render_template("books.html", books=books)


@app.route("/cart", methods=["GET", "POST"])
def cart():

    # Ensure cart exists
    if "cart" not in session:
        session["cart"] = []

    # POST
    if request.method == "POST":
        id = request.form.get("id")
        if id:
            session["cart"].append(id)
        return redirect("/cart")

    # GET
    books = db.execute("SELECT * FROM books WHERE id IN (?)", session["cart"])
    return render_template("cart.html", books=books)
```

templates/layout.html
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>store</title>
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>
```

templates/books.html
```
{% extends "layout.html" %}

{% block body %}

<h1>Books</h1>
{% for book in books %}
	<h2>{{ book["title"] }}</h2>
	<form action="/cart" method="post">
		<input name="id" type="hidden" value="{{ book["id"] }}">
		<button type="submit">Add to Cart</button>
	</form>
{% endfor %}

{% endblock %}
```
- Notice that `cart` is implemented using a list. Items can be added to this list using the `Add to Cart` buttons in `books.html`. When clicking such a button, the `post` method is invoked, where the `id` of the item is appended to the `cart`. When viewing the cart, invoking the `get` method, SQL is executed to display a list of the books in the cart.

## APIs
- An _application program interface_ or _API_ is a series of specifications that allow you to interface with another service. For example, we could utilize IMDB’s API to interface with their database. We might even integrate APIs for handling specific types of data downloadable from a server.

app.py
```
# Searches for shows using Ajax

from cs50 import SQL
from flask import Flask, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///shows.db")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        shows = db.execute("SELECT * FROM shows WHERE title LIKE ? LIMIT 50", "%" + q + "%")
    else:
        shows = []
    return render_template("search.html", shows=shows)
```

templates/search.html
```
{% for show in shows %}
    <li>{{ show["title"] }}</li>
{% endfor %}
```

templates/index.html
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>shows</title>
    </head>
    <body>

        <input autocomplete="off" autofocus placeholder="Query" type="search">

        <ul></ul>

        <script>

            let input = document.querySelector('input');
            input.addEventListener('input', async function() {
                let response = await fetch('/search?q=' + input.value);
                let shows = await response.text();
                document.querySelector('ul').innerHTML = shows;
            });

        </script>

    </body>
</html>
```

- Notice an event listener is utilized to dynamically query the server to provide a list that matches the title provided. This will locate the `ul` tag in the HTML and modify the web page accordingly to include the list of the matches. 
- You can read more in the [AJAX documentation](https://api.jquery.com/category/ajax/).

## JSON
- _JavaScript Object Notation_ or _JSON_ is text file of dictionaries with keys and values. This is a raw, computer-friendly way to get lots of data.
- JSON is a very useful way of getting back data from the server.

index.html
```
<!DOCTYPE html>

<html lang="en">
    <head>
        <meta name="viewport" content="initial-scale=1, width=device-width">
        <title>shows</title>
    </head>
    <body>

        <input autocomplete="off" autofocus placeholder="Query" type="text">

        <ul></ul>

        <script>

            let input = document.querySelector('input');
            input.addEventListener('input', async function() {
                let response = await fetch('/search?q=' + input.value);
                let shows = await response.json();
                let html = '';
                for (let id in shows) {
                    let title = shows[id].title.replace('<', '&lt;').replace('&', '&amp;');
                    html += '<li>' + title + '</li>';
                }
                document.querySelector('ul').innerHTML = html;
            });

        </script>

    </body>
</html>
```
- While the above may be somewhat cryptic, it provides a starting point for you to research JSON on your own to see how it can be implemented in your own web applications.
- You can read more in the [JSON documentation](https://www.json.org/json-en.html).
