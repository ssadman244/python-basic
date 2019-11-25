def hello(first_name, last_name):
    print(f"Hello {first_name} {last_name} !")
    print("What's up?")

print('Start...')
hello("Sadman", "Sakib")
#****************Keyword Arguments*************
hello(last_name="McDonie", first_name="Nancy")
print("")

#************Return*****************

def power(num):
    return num ** num

print(power(3))