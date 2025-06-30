n = int(input('Enter number of elements in an array: '))
try:
    numbers = [float(num) for num in input().split()]   # attaines the value of list
    print(numbers)
    # Normal execution continues 
except ValueError as err:
    print('You may have netered a wrong  float value')









'''
l1.sort(reverse=True)      it prints in descending order '''



