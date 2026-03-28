mango = 2

# addition

# mango = mango + 2 is same mango += 2
# mango += 2

# Substraction

# mango = mango - 2 is same mango -= 2

# multiplication

# mango = mango * 2 is same mango *= 2


# division
# mango = mango / 2 is same mango /= 2

# exponent

#mango = mango ** 3

# to get number is even or odd
reminder = mango % 2

print(reminder)

print(mango)



x = 3.14
y = 4
z = 6
p = -4

result_round = round(x)
print(result_round)

result_absolute = abs(p)
print(result_absolute)

max_result = max(x,y,z,p)
print(max_result)

min_result = min(x,y,z,p)
print(min_result)


import math

print(math.pi)
print(math.e)
print(math.sqrt(y))
print(math.ceil(x))
print(math.floor(x))

print(math.pow(y,2))  # y ki power 2

# find the value of c in triagele

a = float(input("please enter value of side a : "))
b = float(input("please enter value of side b : "))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))

print(f"missing side of triagle size is : {c}")