def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks) if marks else 0
    return total, average
marks = [85, 90, 78, 88, 92]
total, average = sum_avg(marks)
print(f"Total: {total}")
print(f"Average: {average}")
