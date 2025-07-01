#  Find Factorial of a number

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) 


n = int(input('Enter the number: '))
result = factorial(n)
print(f'Factorial of {n} is: {result}')