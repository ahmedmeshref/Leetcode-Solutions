def FirstReverse(strParam):
    reversedStr = ""
    for i in range(len(strParam) - 1, -1, -1):
        reversedStr += strParam[i]
    # code goes here
    return reversedStr


# keep this function call here
print(FirstReverse(input()))
