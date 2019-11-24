numbers = [5, 2, 5, 2, 2]
#*************************************
for a in numbers:
    print("*" *a)
print("")
#*************************************
for x in numbers:
    temp = f"{x}"
    for y in temp:
        temp1 = int(y)
        print("*" * temp1)
print("")
#****************************************
for x_count in numbers:
    output = ""
    for y_count in range(x_count):
        output += "*"
    print(output)