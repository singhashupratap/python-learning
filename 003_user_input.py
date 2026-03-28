# name = input("What is your name : ")
# age = int(input("whatis your age : "))


name = input("What is your name : ")

while True:
    try:
        age = int(input("What is your age : "))
        break  # valid input → exit loop
    except ValueError:
        print("❌ Please enter a valid integer (no decimals or text).")

print(f"Hello {name}, your age is {age}")