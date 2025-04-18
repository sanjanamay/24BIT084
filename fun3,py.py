def create_array(x, y, z value):
    
     return[[[value for _ in range(z)]for _ in range(y)]for _ in range(x)]

array = create_array(6, 7, 8, 9)

for layer in array:
    for row in layer:
        print(row)
    print()
    
    
