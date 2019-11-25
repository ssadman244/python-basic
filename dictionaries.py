customers = {
    "name" : "Sadman",
    "age" : 21,
    "dob" : "25 August, 1998",
    "phone" : '01897738',
}

print(customers["name"])
print(customers.get('dob'))

customers["name"] = "Sakib"

print(customers.get("name"))