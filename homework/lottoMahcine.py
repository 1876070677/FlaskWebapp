import random

userNums = [1, 2, 3, 4, 5]
randNums = [5, 4, 3, 2, 1]
collect = []

def setUNumbers(ns):
    global userNums
    userNums = ns

def getUNumbers():
    return userNums

def setRNumbers():
    global randNums

    randNums = random.sample(range(1, 46), 6)

def getRNumbers():
    return randNums

def compareNumbers():
    global userNums
    global randNums
    global collect

    collect = []
    for item in userNums:
        if randNums.count(item) != 0:
            collect.append(item)

    return collect

print(compareNumbers())