try:
    age = int(input("Age : "))
    num = 1000
    age = num // age
    print(age)
except ValueError:
    print("Invalid input type")
except ZeroDivisionError:
    print("Age can't be 0")