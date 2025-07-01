#  Find sum of list elements

sum = 0
list = list(map(int,input('Enter list elements: ').split()))

for num in list:
    sum += num
    num += 1

print('Sum of list elements: ',sum)
