names_set = {"Alice", "Bob", "Adam", "Ben", "Charlie", "Bella", "Andrew", "Brian"}
names_starting_with_A = {name for name in names_set if name.startswith('A')}
names_starting_with_B = {name for name in names_set if name.startswith('B')}
print("Names starting with A:", names_starting_with_A)
print("Names starting with B:", names_starting_with_B)
