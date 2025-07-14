# Find sum of the series: n - n^2/3 + n^4/5 - n^8/7 + ... up to m terms

n = int(input('Enter N (term) value (1 <= n <= 4): '))
m = int(input('Enter number of terms (2 <= m <= 10): '))

# Validate input (optional but recommended)
if not (1 <= n <= 4 and 2 <= m <= 10):
    print("Invalid input. Please ensure 1 <= n <= 4 and 2 <= m <= 10.")
else:
    sum_of_series = 0
    sign = 1  # Start with positive term

    for i in range(m):
        exponent = 2 ** i
        numerator = n ** exponent
        denominator = 2 * i + 1
        term = sign * (numerator / denominator)
        sum_of_series += term
        sign *= -1  # Alternate the sign

    print("Sum of the series:", sum_of_series)
