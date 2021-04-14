# Encryption methods

- Listerer indexerer
The listerer indexerer encryption method takes a list of numbers which have a maximum value and converts it into the index it would have in an imaginary list of all possible combinations of that list, and that way it can be used to generate the list again.

Example:
  Given the list [20, 40, 250], with a max value of 255, it will give the 'imaginary index' it would have, this is very simply given by the formula:
    
    being i a given item's position of the list
    n the length of the list
    p the max value
    going from i = first item of the list to the n'th
    
    ⅀(p + n - i - 1)^(n - i - 1)
    
  In this case, it would output the value 1331470
  To then get the list back, it would follow this process:
  
    v = given value of 'index' of a list
    p = max possible value of the list
    n = length of the list
    i = iterator
    
    r = v / ((p + n - i - 1)^(n - i - 1)) = 1331470 / ((255 + 3 - 0 - 1)^(3 - 0 - 1)) = 20.158821
    truncate r down, r = 20
    r is our first value of the list [20]
    v = v - ((p + n - i - 1)^(n - i - 1) * r), v = 10490
  
  Repeat this process until v is less than or equal to the max value, in that case, v is the last value of the list.

    r = v / ((p + n - i - 1)^(n - i - 1)) = 10490 / ((255 + 3 - 1 - 1)^(3 - 1 - 1)) = 40.9765
    truncate r down, r = 40
    r is our second value of the list [20, 40]
    v = v - ((p + n - i - 1)^(n - i - 1) * r), v = 250

    v is less than p, therefore v is out last value and our list is complete, [20, 40, 250]

  And as we can see, our initial list is equal to the list we recuperated.
