# simple python script to play around with git commands
import random
#sort array
arr = [5, 1, 3, 2, 4]

print(arr)

random.shuffle(arr)

print(arr)
for x in arr:
    print(x)
    if x == 5:
        print('yes, it have 5 ')
        break