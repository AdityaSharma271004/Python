chai_types = { "masala": "spicy",
"ginger": "zesty", "green": "healty"}
# print(chai_types)
print(chai_types["green"]) #value = healthy
chai_types["green"] = "fresh"
# print(chai_types)
# for chai in chai_types:
    # print(chai)

# for chai in chai_types:
    # print(chai, chai_types[chai])   

# for key, value in chai_types.items():
    # print(key, value)  

# if "masala" in chai_types:
    # print("i have masala chai")    

# print(len(chai_types))
# print(chai_types)

chai_types["earl grey"]="citi"
# print(chai_types)

chai_types.pop("ginger")
# print(chai_types)

chai_types.popitem()
# print(chai_types)

del chai_types["green"]
# print(chai_types)

chai_types_copy = chai_types.copy()
# print(chai_types_copy)

tea_shop = { "chai": {"masala": "spicy", "ginger": "zesty"},
"tea": {"green":"fresh","black":"strong"}}
print(tea_shop)

print(tea_shop["chai"])

print(tea_shop["chai"]["ginger"])

squard_num = {x : x**2 for x in range(10)}
print(squard_num)

print(squard_num.clear())
print(squard_num)

keys = ["masala" , "ginger", "lemon"]
default_values = "delicious"

new_dict = dict.fromkeys(keys, default_values)
print(new_dict)

new_dict = dict.fromkeys(keys, keys)
print(new_dict)
