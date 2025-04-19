list1 = [5, 10, 15, 20, 25, 30]
list2 = [10, 20, 30, 40, 50]

list3 = [num for num in list1 if num not in list2]
list3.sort()
print("Numbers in list1 but not in list2:", list3)
