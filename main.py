def DetermineAmount(binaryCode):
    binaryStrings = binaryCode.split(",")
    originString = binaryStrings[0]
    print(binaryStrings)
    for string in binaryStrings:
        if(len(string) != len(originString)):
            return "all strings in binary code must be the same length"
        for bit in string:
            if bit not in ["0","1"]:
                return "invalid bit string within binary code"
    distance = 0
    allDistances = []
    for string in binaryStrings:
        for i in range(len(originString)):
            if originString[i] != string[i]:
                distance+=1
        if distance != 0:
            allDistances.append(distance)

    C = min(allDistances)
    amntErrors = C-1
    amntCorrections = int((C-1)/2)

    return("the max amount of errors is "+ str(amntErrors) +" and the max amount of corrections is "+ str(amntCorrections))


if __name__ == '__main__':
    userBinaryCode = input("enter binary code, separate each string with comma\n")
    print(DetermineAmount(userBinaryCode))
