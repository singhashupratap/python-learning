# type casting is converting data type of a variable from a one data type to another data type

name = "Ashutosh Singh"
age = 35
gpa = 9.9
is_employer = False


print(f"my current age is {age} and data type is {type(age).__name__}, but I converted it's data type from int to float {float(age)} "
      f"and now my age is {type(float(age)).__name__}")


print(int(gpa))

print(int(is_employer))