# Listerer Indexerer

The "listerer indexerer" is an encryption method designed and implemented by me, which works by converting a list of bytes from a file into an integer, that can be seen as an "index" to the position where this list would be found in an array of all possible permutations of the numbers from said list.

Example:
  Given the list [20, 40, 250], with a max value of 255, the function 'findListIndex' will return the 'imaginary index' it would have, this is given by the formula:
    
    N = Length of the list
    P = Maximum value that could be in the list
    I = Iterator starting at 0 and increasing until it reaches the size of the list
    
    ⅀(P + N - I - 1)^(N - I - 1)
    
  In this case, the list's index would be 1331470
  To then get the list back, the function 'indexererListerer' would follow this process:
  
    V = Value of 'index' of a list
    N = Maximum value that could be in the list
    N = Length of the list
    I = Iterator starting at 0 and increasing until it reaches the size of the list
    
    R = V / ((P + N - I - 1)^(N - I - 1))       || 1331470 / ((255 + 3 - 0 - 1)^(3 - 0 - 1)) = 20.158821
    Truncate R downwards                        || R = 20
    R is the first value of the list            || [20]
    V = V - ((P + N - I - 1)^(N - I - 1) * R)   || V = 10490
  
  Repeat this process until V is less than or equal to P, in which case V is the last value of the list.

    R = V / ((P + N - I - 1)^(N - I - 1))     || 10490 / ((255 + 3 - 1 - 1)^(3 - 1 - 1)) = 40.9765
    Truncate R downwards                      || R = 40
    R is the second value of our list         || [20, 40]
    V = V - ((P + N - I - 1)^(N - I - 1) * R) || V = 250

    V is now less than P, therefore V is out last value and our list is complete [20, 40, 250]

  And as we can see, our initial list is equal to the list we recuperated.
  
  
EXAMPLES:

![alt text](https://github.com/Pharadas/encryption_methods/blob/main/ListererIndexerRandomListExample.PNG?raw=true)

![alt text](https://github.com/Pharadas/encryption_methods/blob/main/image.png?raw=true)
