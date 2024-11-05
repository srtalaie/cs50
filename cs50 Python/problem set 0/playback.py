# Accept user input and store in variable
user_input = input("What do you want to say? ")

# Strip leading and trailing white space from user input
user_input = user_input.strip()

# Add "..." instead of whitespace between words
user_input = user_input.replace(" ", "...")

print(user_input)
