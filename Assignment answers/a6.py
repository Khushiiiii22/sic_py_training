#  Check if a +ve integer is Perfect square

                               
import math

positive_integer = int(input('Enter number: '))

if math.isqrt(positive_integer) ** 2 == positive_integer:
    print(positive_integer, 'is a perfect square')
else:
    print(positive_integer, 'is not a perfect square')
