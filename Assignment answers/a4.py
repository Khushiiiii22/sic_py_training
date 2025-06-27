# Print the Prime numbers in decreasing order between m and n (m < n)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Take input
m = int(input("Enter the value of m (smaller number): "))
n = int(input("Enter the value of n (larger number): "))

# Validate input
if m < 2:
    print('Please enter m greater than or equal to 2.')
elif m >= n:
    print('Please make sure that m is less than n.')
else:
    print(f"Prime numbers between {m} and {n} in decreasing order:")
    for i in range(n, m - 1, -1):
        if is_prime(i):
            print(i, end=' ')
