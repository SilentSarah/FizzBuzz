
# FizzBuzz from 42's exams made in python
# difficulty level: Pretty Low
# requirements: conditions, input, loops
# Dev: SSarah - Sarah Hicham Meftah
# Date: 05/09/2022

start = input("Put the starting number in the prompt:\n")

if int(start) < 0 :
    start = input("Put the starting number in the prompt:\n")

end = input("Put the limit here:\n")

if int(end) <= 0 :
    end = input("Put the limit here:\n")

startI = int(start)
endI = int(end)

while startI <= endI:
    if startI == 0:
        print(startI)
    elif startI % 5 == 0 and startI % 3 == 0 :
        print("fizzbuzz")
    elif startI % 5 == 0 :
        print("buzz")
    elif startI % 3 == 0 :
        print("fizz")
    else :
        print(startI)
    startI += 1