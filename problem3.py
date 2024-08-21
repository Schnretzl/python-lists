# 3. Advanced Slicing Techniques

# Task 1: Extract the temperatures for the second week (7 days) of the month (index 7 to index 14).
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week = temperatures[7:14]
print(f"Second week temperatures: {second_week}")

# Task 2: Extract all the temperatures above 100.
# Note: I was unsure whether to address temperatures > 100 or >= 100. I chose the former as the problem states "above 100" as opposed to "at least 100".
above_100 = temperatures[-6:]
print(f"Temperatures over 100: {above_100}")