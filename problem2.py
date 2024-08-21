# 2. Advanced List Methods and Identity Operators

# Task 1: Find out if Alice submitted their assignment and attended class.
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

print("Alice submitted their assignment and attended class" \
      if "Alice" in submitted and "Alice" in attended else \
      "Alice either did not submit their assignment or did not attend class")