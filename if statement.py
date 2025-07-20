# write a program to bucket age

age = int(input("Please enter your age : "))

if age < 18 :
    print("Sorry! you are not eligible waiting until you turn 18")
elif age >= 18 and age < 25:
    print("Yeahh your are eligible but you will get less credit limit")
elif age >= 25 and age <= 60:
    print("You are perfect customer for us")
elif age > 60 :
    print("you are old Sorry ")
else:
    print("enter correct age between 18 to 60")


############## if not

is_sunny = False

if not is_sunny :
    print("it's hot outside")
else :
    print("bhaggggg ")



a = 10
b = 20
print("Positive" if a > b else "Negative")

num = 13
print("EVEN" if num % 2 == 0 else "ODD")