
# FizzBuzz from 42's exams made in python
# difficulty level: Pretty Low
# requirements: conditions, input, loops
# Dev: SSarah - Sarah Hicham Meftah
# Date: 05/09/2022

startI = 0
endI = 1000

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
