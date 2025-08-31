tea_types = ("black","green", "oolong")
print(tea_types)

print(tea_types[0])

print(len(tea_types))

more_tea = ("herbal", "white")
all_tea = more_tea + tea_types
print(all_tea)

if "green" in all_tea:
    print("i have green tea")

print(type(tea_types))