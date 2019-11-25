message = input("> ")
mess_list = message.split(" ")
str = ""

emoji = {
    ":)": ":)",
    ":(": ":("
}
for i in mess_list:
    str += emoji.get(i, i) + " "
print(str)