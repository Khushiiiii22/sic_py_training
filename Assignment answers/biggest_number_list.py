#  Find biggest element in an list of n numbers.

list = [2 , 6 , 7 , 9 , 3 , 5 , 6]
max=0

for i in list:
    if i >= max:
        max = i
print('Biggest element is:',max)
    
