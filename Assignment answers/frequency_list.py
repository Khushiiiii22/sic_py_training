# Find the frequency an element in a list of n elements.

list = [1 , 3 , 5 , 5 , 5 , 7 , 7 , 8 , 9 , 9 , 9]
number = int(input('Enter number to check: '))
count = 0

for num in list:
    if num == number:
        count += 1
if count > 0:
    print('The frequency of ',number,'is',count)

else:
    print('Number is not present in the list')



