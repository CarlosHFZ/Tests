def reverse_string(input_string):
    reversed_string = ""

    for char in input_string[::-1]:
        reversed_string += char

    return reversed_string


user_input = input("Enter a string: ")
reversed_result = reverse_string(user_input)
print(f"Reversed string: {reversed_result}")