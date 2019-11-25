numbers = [1, 1, 3, 3, 4, 5, 6, 3, 6, 0, 8, 9, 8, 50]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)
print(unique)
unique.sort()
print(unique)