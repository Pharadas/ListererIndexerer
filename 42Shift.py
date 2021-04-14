def shift42Encrypt():
    readFile = open("TestTextEncrypted.txt", "rb")
    encryptedFile = open("TestTextDeEncrypted.txt", "wb")
    valuesToUse = [i for i in range(1, 100, 5)]

    # for r in valuesToUse:
    #     byte = readFile.read(1)
    #     while byte:
    #         bytes42 = []
    #         for i in range(r):
    #             bytes42.append(byte)
    #             byte = readFile.read(1)
    #         for i in reversed(bytes42):
    #             encryptedFile.write(i)

    bytesList = []
    byte = readFile.read(1)
    while byte:
        bytesList.append(byte)
        byte = readFile.read(1)

    for p in valuesToUse:
        x = 0
        y = 0
        for i in bytesList:
            if x == p:
                bytesList[x:y] = reversed(bytesList[x:y])
                x = y
                
            else:
                x += 1

    for i in reversed(bytesList):
        encryptedFile.write(i)

    encryptedFile.close()
    readFile.close() 
shift42Encrypt()
