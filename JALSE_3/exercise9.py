python
list1 = input("Please enter the first list (e.g., [1, 2, 3]): ")
list2 = input("Please enter the second list (e.g., [4, 5, 6]): ")

list1 = eval(list1)
list2 = eval(list2)

result = list(map(lambda x, y: x + y, list1, list2))

print("Resulting list:", result)
