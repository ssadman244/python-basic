numbers = [10, 20, 30, 100, 200, 4000, 2099, 10000, 50, 89000, 1, 789]
largest = numbers[0]
for number in numbers:
    if number > largest:
        largest = number
print(largest)