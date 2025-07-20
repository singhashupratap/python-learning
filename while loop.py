name = str(input("Please enter your name : "))

while name == "" :
    print("Blank name will not acceptable")
    name = str(input("Please enter your name : "))
print(f"Welcome {name} on board")



######## Favorite food

food = str(input("Please enter the food name you like (q to quite) : ")).lower()

while not food == "q":
    print(f"Thanks for odering your favourite {food}")
    food = str(input("Please enter another food that you like (q to quite : ")).lower()
print("Thaks for visting hope we can serve you better next time ")

##### Compound interest calculation

principal = int(input("Please enter the Principal Amount : ₹"))
while principal <= 0 :
    print("Not a valid principal amount")
    principal = int(input("Please enter the Principal Amount in positive and non zero : "))

rate = float(input("Please enter rate of interest : %"))
while rate <= 0 :
    print("Not a valid rate of interest")
    rate = float(input("Please enter the rate of interest in positive and non zero : "))

time = float(input("Please enter the time in year/s for investment : "))
while time <= 0 :
    print("Not a valid year/s")
    rate = float(input("Please enter the year/s in positive and non zero : "))

print(f"\n✅ Summary:")
print(f" Your principal Amount is ₹ {principal}")
print(f" Your rate of interest is {rate}%")
print(f" Your  is {time} year/s")

final = round(principal *pow((1+rate/100),time),2)
print(f"After {time} year/s your ₹{principal} amount will be ₹{final}  at the rate of {rate}%")