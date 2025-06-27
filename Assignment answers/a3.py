#  Count number of Prime digits in a number

prime_digit = input('Enter the number: ')


prime_digits = ['2', '3', '5', '7']

count = 0

for i in prime_digit:
    if i in prime_digits:
        count += 1

print('The number of prime digits are:', count)   