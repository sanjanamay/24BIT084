my_tuple = (10, 20, 30)
temp_list = list(my_tuple)
temp_list[1] = 25
modified_tuple = tuple(temp_list)
print("Original tuple:", my_tuple)
print("Modified tuple:", modified_tuple)
