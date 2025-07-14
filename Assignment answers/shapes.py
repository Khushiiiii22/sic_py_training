'''Print the following shapes by accepting number of lines
A. Right Angled Triangle
B. Equi lateral Triangle
C. Hollow Square
D. Howllow Rhombus
E. Pascal's Triangle
F. X shape
G. X shape inside hollow Square with 0 at middle/center
H. Benzene Ring (C6H6) Hexagon '''


def right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def equilateral_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def hollow_rhombus(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def pascals_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        num = 1
        for j in range(i + 1):
            print(f'{num} ', end='')
            num = num * (i - j) // (j + 1)
        print()

def x_shape(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

def x_in_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == n - i - 1 or i == 0 or i == n - 1 or j == 0 or j == n - 1:
                if n % 2 == 1 and i == n // 2 and j == n // 2:
                    print('0', end='')
                else:
                    print('*', end='')
            else:
                print(' ', end='')
        print()

def benzene_ring(n):
    # crude representation of hexagon (C6H6)
    if n < 3:
        print("Minimum lines should be 3 to draw hexagon")
        return
    print(' ' * (n + 1) + '/\\')
    for i in range(n):
        print(' ' * (n - i) + '/' + ' ' * (2 * i + 2) + '\\')
    for i in range(n):
        print(' ' * (i + 1) + '\\' + ' ' * (2 * (n - i - 1) + 2) + '/')
    print(' ' * (n + 1) + '\\/')

# --- Main Menu ---
def main():
    print("""
    Choose a shape to print:
    A. Right Angled Triangle
    B. Equilateral Triangle
    C. Hollow Square
    D. Hollow Rhombus
    E. Pascal's Triangle
    F. X Shape
    G. X Shape inside Hollow Square with 0 at center
    H. Benzene Ring (Hexagon)
    """)
    
    choice = input("Enter your choice (A-H): ").strip().upper()
    lines = int(input("Enter number of lines: "))

    print("\nGenerated Shape:\n")
    if choice == 'A':
        right_angled_triangle(lines)
    elif choice == 'B':
        equilateral_triangle(lines)
    elif choice == 'C':
        hollow_square(lines)
    elif choice == 'D':
        hollow_rhombus(lines)
    elif choice == 'E':
        pascals_triangle(lines)
    elif choice == 'F':
        x_shape(lines)
    elif choice == 'G':
        x_in_hollow_square(lines)
    elif choice == 'H':
        benzene_ring(lines)
    else:
        print("Invalid choice!")

if __name__ == '__main__':
    main()
