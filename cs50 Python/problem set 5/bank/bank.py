user_input = input("Greeting: ")

# Clean string and make all letters lowercase
user_input = user_input.strip().lower()

# Split string by words and get the first word as the greeting
user_input_array = user_input.split(" ")
greeting = user_input_array[0]

# Split the greeting into chars and get the first letter
greeting_array = [*greeting]
first_letter = greeting_array[0]

if "hello" in greeting:
    print("$0")
elif first_letter == "h":
    print("$20")
else:
    print("$100")
