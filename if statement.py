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