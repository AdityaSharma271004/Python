tea_varities = ["Buck", "green", "ginger", "white"]
print(tea_varities)
print(tea_varities[-1])
print(tea_varities[:2])
tea_varities[3] = "herbal"
print(tea_varities)
print(tea_varities[1:2])
tea_varities[1:2] = ["lemon"]
print(tea_varities)
for tea in tea_varities:
    print(tea)
for tea in tea_varities:
    print(tea, end="-")   

tea_varities.append("mango")
print(tea_varities)
if "mango" in tea_varities:
    print("i have mango tea")
tea_varities.pop()
print(tea_varities)    
tea_varities.remove("ginger")
print(tea_varities)
tea_varities.insert(1,"ginger")
print(tea_varities)
tea_copy = tea_varities.copy()
print(tea_copy)
tea_copy.append("greeen")
print(tea_varities)
print(tea_copy)
nums = [x**2 for x in range(10)]
print(nums)