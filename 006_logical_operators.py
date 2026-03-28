# logical operators = evaluate multiple condition (or, and, not)
from os import access

# not == invert the condition (not false, not true)


# temp = 19
# is_rain = True
# is_sunny = False
#
# if (temp > 20 and is_sunny) or is_rain:
#     print("outdoor program cancelled")
# else:
#     print("outdoor program is still scheduled")



# conditional expression

# a = 10
# b = 20
# print("Positive" if a > b else "Negative")

# num = 13
# print("EVEN" if num % 2 == 0 else "ODD")


user_role = "guestweddd"

access_level = "Full Access" if user_role == "admin" else  "lmited access"

access_level = "Full Access" if user_role == "admin" \
                else  "lmited access" if user_role == "guest" \
                else "No access"

print(access_level)