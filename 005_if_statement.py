# write a program to bucket age

# age = int(input("Please enter your age : "))

# if age < 18 :
#     print("Sorry! you are not eligible waiting until you turn 18")
# elif age >= 18 and age < 25:
#     print("Yeahh your are eligible but you will get less credit limit")
# elif age >= 25 and age <= 60:
#     print("You are perfect customer for us")
# elif age > 60 :
#     print("you are old Sorry ")
# else:
#     print("enter correct age between 18 to 60")


############## if not

# is_sunny = False
#
# if not is_sunny :
#     print("it's hot outside")
# else :
#     print("bhaggggg ")





#  weight conversion program
# unit_type = str(input("please enter unit of weight kg or lb : "))
# weight = round(float(input("please enter your weight : ")),2)
#
# if unit_type == "kg":
#     print(f"your weight in Kg is {weight} and in pounds {round(weight * 2.205,2)} lb")
# elif unit_type == 'lb':
#     print(f"your weight in lb is {weight} and in pounds {round(weight * 0.4536,2)} kg")
# else:
#     print("choose only kg or lb")


# Calculator

operation = input("please choose any out of this (+,-,/,*,%) : " )

num_1 = float(input("please enter the first number : "))
num_2 = float(input("please enter the second number : "))

if operation == "+":
    print(f"You choose addition here is result {num_1 + num_2}")
elif operation == "-":
    print(f"You choose substraction here is result {num_1 - num_2}")
elif operation == "/":
    print(f"You choose devision here is result {round(num_1/num_2,2)}")
elif operation == "*":
    print(f"You choose multiplication here is result {round(num_1 * num_2,2)}")
elif operation == "%":
    print(f"You choose reminder here is result {round(num_1%num_2,2)}")
else:
    print("Choose only given operators")