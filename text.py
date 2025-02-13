from time import time
import random as r

def mistake(partest, usertest):
    error = 0
    # Iterate over the characters of both strings up to the length of the shortest one
    for i in range(min(len(partest), len(usertest))):
        if partest[i] != usertest[i]:
            error += 1
    # If the strings have different lengths, count the additional characters as errors
    error += abs(len(partest) - len(usertest))
    return error

def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput.split()) / time_R  # Words per second
    return round(speed, 2)

# Sample text
test = ["this is priyanka" ,
        "i am writing my first python project",
       "this is the text speed calculator."]
test1 = r.choice(test)   # Randomly choose one sentence

print("*******typing speed*******")
print(test1)
print()  # Line break

time_1 = time()

testinput = input("Enter: ")
time_2 = time()
# Calculate and print typing speed and mistakes
print('Speed:', speed_time(time_1, time_2, testinput), "w/sec")  # w/sec is words per second
print("Error:", mistake(test1,testinput))






