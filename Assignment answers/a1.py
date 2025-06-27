# Find the biggest digit in a number

biggest_number = input('Enter the number: ')

max = '0'
for i in biggest_number:
    if i > max:
        max = i

print('The biggest digit is:', max )
        
