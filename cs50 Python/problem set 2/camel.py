user_input = input("camelCase: ")
camel_case_list = list(user_input)

for letter in range(len(camel_case_list)):

    if camel_case_list[letter].isupper():
        camel_case_list[letter] = camel_case_list[letter].lower()
        camel_case_list.insert((letter), "_")

snake_case = "".join(camel_case_list)

print("snake_case: ", snake_case)
