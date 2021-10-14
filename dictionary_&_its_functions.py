# Dictionary and its functions

d1={"Sid": "Mankar", "Satyam": "M", "Mom":"Yogita",
     "GPN":{"Janhavi": "Sonawane", "Vaishnavi": "Saindane"}, "Tuple":(1,3,4)}
print(type(d1))
print(d1["GPN"])
# del d1["Tuple"]
# print(d1)
# d2=d1.
# del d2["GPN"]
print(d1.get("Sid"))
abc={"Leena": "Toffee"}
d1.update(abc)

# print(d1.keys())
print(d1.items())
