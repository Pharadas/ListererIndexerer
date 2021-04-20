from listererindexer import findListIndex, indexerListerer

def DeEncrypt(filename, size):
    thisThing = filename.split('.')
    encryptedFilename = thisThing[0] + 'Encrypted.' + thisThing[1]
    deEncryptedFilename = thisThing[0] + 'DeEncrypted.' + thisThing[1]
    print(deEncryptedFilename)
    with open(encryptedFilename, 'rb') as readFile:
        with open(deEncryptedFilename, 'wb') as thisFile:
            bytesList = []
            thingBytes = b''
            byte = readFile.read(1)
            thisNum = 0
            while byte:
                # thisNum += 1
                # bytesList.append(int.from_bytes(byte, 'big'))
                bytesList.append(byte)
                thingBytes += byte
                byte = readFile.read(1)
                if len(bytesList) == size + 1:
                    # print(bytesList)
                    bytesObject = b''
                    for i in bytesList:
                        bytesObject += i
                    # print(bytesObject)
                    newBytesList = indexerListerer(int.from_bytes(bytesObject, 'big'), size, 255)
                    newBytesObject = b''
                    for i in newBytesList: 
                        newBytesObject += i.to_bytes(1, 'big')
                    # print(newBytesObject)
                    thisFile.write(newBytesObject)
                    bytesList = []
                    # print(thisNum, end='\r')
                    
def encrypt(filename, size):
    thisThing = filename.split('.')
    encryptedFilename = thisThing[0] + 'Encrypted.' + thisThing[1]
    with open(filename, 'rb') as readFile: # textExecutable.exe
        with open(encryptedFilename, 'wb') as thisFile:
            bytesList = []
            byte = readFile.read(1)
            bytesThingie = b''
            # waiting = 0
            while byte:
                bytesList.append(int.from_bytes(byte, 'big'))
                byte = readFile.read(1)
                if len(bytesList) == size:
                    # print(bytesList)
                    this = findListIndex(bytesList, 255)
                    # print(this)
                    this = this.to_bytes(5, 'big')
                    # print(this)
                    # print(indexerListerer(int.from_bytes(this, 'big'), 5, 255))
                    bytesList = []
                    thisFile.write(this)
                    
encrypt('TestText.txt', 4)
DeEncrypt('TestText.txt', 4)
