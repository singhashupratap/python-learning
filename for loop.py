# A for loop lets you repeat a task for fixed numbers of times

for x in range (1, 11) :
    print(x)

for x in range (1, 21, 2) :
    print(x)

for x in reversed( range(0, 11)) :
    print(x)
print("Happy New Year")

# will terminate loop at 13
for x in range(1, 21):
    if x == 13:
        break
    print(x)

# ### will skip
for x in range (1, 21) :
    if x == 13 :
        continue
    print(x)


# counter
import time

spend_time = int(input("please enter the time in seconds : "))
print("Time started")
for x in reversed(range(1,spend_time )) :
    print("Time left ", x)
    time.sleep(1)
print("Times up")

# Digital clock

spend_time = int(input("please enter the time in seconds : "))
print("Time started")
for x in range(spend_time, 0, -1) :
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Times up")