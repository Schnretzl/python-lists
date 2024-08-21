# 1. Python List Transformation

# Task 1: Sort the grades in descending order and print the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
print(f"Grades in descending order: {grades}")


# Task 2: Calculate the average grade and print it.
average = sum(grades) / len(grades)
print(f"Average: {average}")