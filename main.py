import random


foundNameCounter = 0
foundNameAgain = True
arraySize = 0
ix = 0

namesArray = ["damian", "stanisław", "karol", "bartosz", "dariusz", "tomasz", "daniel", "jakub", "wojciech", "piotr"]

try:
    while arraySize <= 0:
        print("Enter array size: ")
        arraySize = int(input())
        if arraySize <= 0:
            print("Arrays size must be bigger then 0!")

    namesFilled = []

    for i in range(arraySize):
            namesFilled.append(namesArray[random.randint(0, len(namesArray)-1)])

    print("This are all names that has been generated:")
    nameNumber = 1
    for names in namesFilled:
        print("Name number " + str(nameNumber) + " is: " + names)
        nameNumber += 1

    while foundNameAgain == True:
        ix = 0
        foundNameCounter = 0
        foundNameAgain = True

        print("Enter name to found and I will count how many times it has been found in random names array: ")
        nameToFound = input()
        nameToFound = nameToFound.upper()

        for i in namesFilled:
            namesFilled[ix] = i.upper()
            ix += 1

        for x in namesFilled:
            if x.upper() == nameToFound:
                foundNameCounter += 1

        print("Name " + nameToFound + " has been found: " + str(foundNameCounter) + " times in all generated names.")
        print("Do You want to found other name? (Y/N)")
        againFounder = input()
        againFounder = againFounder.upper()
        if againFounder == "N":
            foundNameAgain = False
except:
    print("An exception occurred")