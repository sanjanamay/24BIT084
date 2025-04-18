def compute(n):
    str_n = str(n)
    result = int(str_n), int(str_n * 2), int(str_n * 3), int(str_n *4)
    return result

for i in range(4, 8):
  print(f"compute({i}) = {compute(i)}")

