# Convert instances of :) or :( to their respective emojis and return the string
def convert(str):
    str = str.replace(":)", "🙂")
    str = str.replace(":(", "🙁")
    return str


def main():
    user_input = str(input("What would you like to say? "))
    user_input = user_input.strip()
    user_input = convert(user_input)
    print(user_input)


main()
