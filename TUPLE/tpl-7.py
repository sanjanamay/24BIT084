my_tuple = (10, 20, 30, 40)
temp_list = list(my_tuple)
del temp_list[2]
new_tuple = tuple(temp_list)
print("Original tuple:", my_tuple)
print("Tuple after deletion:", new_tuple)
