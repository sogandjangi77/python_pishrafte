python
input_data = input("Please enter a list of numbers (e.g., [1, 2, 3, 4, 5]): ")

number_list = eval(input_data)

even_numbers = list(filter(lambda x: x % 2 == 0, number_list))

print("Even numbers:", even_numbers)
