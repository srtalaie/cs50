from validator_collection import checkers, errors, validators


def main():
    print(email_check(input("What's your email address? ")))


def email_check(s):
    try:
        email = validators.email(s)
        if email:
            return "Valid"
        else:
            return "Invalid"
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    except ValueError:
        return "Invalid"


if __name__ == "__main__":
    main()
