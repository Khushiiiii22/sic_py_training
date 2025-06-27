# Find the 2nd smallest digit in a number

second_smallest_digit = input('Enter the number')

number = sorted(set(second_smallest_digit))   #sort the numbers in arranging order to find digits easily

if len(number) > 1:
    print('Second smallest digit is', number [1])
 