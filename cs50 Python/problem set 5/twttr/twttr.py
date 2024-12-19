user_input = list(input("Input: "))
vowels = ["a", "e", "i", "o", "u"]
output_list = []

for i in range(len(user_input)):
    if user_input[i].lower() not in vowels:
        output_list.append(user_input[i])


output = "".join(output_list)
print("Output:", output)
