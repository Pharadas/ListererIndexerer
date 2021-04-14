import random as rndm

print('please give the input to generate random lists within your specifications')
sizeOfList = int(input('size of list? '))
maxValueOfList = int(input('max value of list? '))

this = True
while this:
    print('###########################################################################')
    thisList = [rndm.randint(0, maxValueOfList) for i in range(sizeOfList)]
    # thisList = [14, 16, 28, 7, 12, 26, 20, 0, 5, 0]

    print(thisList)

    def findListIndex(thisList, maxValue):
        n = len(thisList) - 1
        thisSum = 0
        for i in thisList:
            thisSum += (((maxValue + n) ** n) * i)
            n -= 1
        return thisSum

    listIndex = findListIndex(thisList, maxValueOfList)
    print(listIndex)

    # pasar uno menos la longitud de la lista en listLength
    def indexerListerer(index, listLength, maxValue):
        listToReturn = []
        listLength -= 1
        while True:
            if listLength == 0:
                listToReturn.append(int(index))
                break

            thisValue = (maxValue + listLength)**(listLength)
            r = (index) / thisValue
            r = int(r)

            index = index - (thisValue * r)

            listToReturn.append(r)

            listLength -= 1

            print(index, (index) / thisValue, '            ', listToReturn)

        return listToReturn

    newList = indexerListerer(listIndex, len(thisList), maxValueOfList)
    print(newList)

    if newList != thisList:
        print("the recuperated list isnt equal to original list, can u raise issue or send me list or smthn???")
        break
    else:
        print('recuperated list is equal to initial list')
        if input('continue? y/n ') == 'n':
            break

#######################################################

# thisList = [20, 40, 250]
# # thisList = [rndm.randint(0, 30) for i in range(3)]

# print(thisList)


# def findListIndex(thisList, maxValue):
#     n = len(thisList) - 1
#     thisSum = 0
#     for i in thisList:
#         thisSum += (((maxValue + n) ** n) * i)
#         n -= 1
#     return thisSum


# listIndex = findListIndex(thisList, 255)
# print(listIndex)

# # pasar uno menos la longitud de la lista en listLength


# def indexerListerer(index, listLength, maxValue):
#     listToReturn = []
#     listLength -= 1
#     while True:
#         if listLength == 0:
#             listToReturn.append(int(index))
#             break

#         thisValue = (maxValue + listLength)**(listLength)
#         r = (index) / thisValue
#         r = int(r)

#         print(index, listLength, (index) / thisValue)

#         index = index - (thisValue * r)

#         listToReturn.append(r)

#         listLength -= 1

#     return listToReturn


# newList = indexerListerer(listIndex, len(thisList), 255)
# print(newList)
