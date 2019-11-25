numbers = input("Numbers : ")
str = ""
#******************Dictionary*******************
dictionay = {
    "1": 'One',
    "2": 'Two',
    "3": 'Three',
    "4": 'Four',
    "5": 'Five',
    "6": 'Six',
    "7": 'Seven',
    "8": 'Eight',
    "9": 'Nine'
}

for i in numbers:
    temp_str = dictionay.get(i, "!") + " "
    str += temp_str
print(str)