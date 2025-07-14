#  Find smalllest element in an list of n numbers.

list = [2 , 6 , 7 , 4 , 3 , 1 , 6]
min=list[0]

for num in list:
    if num <= min:
        min = num
print('Smallest element is:',min)
    