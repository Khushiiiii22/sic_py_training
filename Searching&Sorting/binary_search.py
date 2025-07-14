# Binary search Using Iterative functions  (do_while)

array = list(map(int,input('Enter the elements of the list: ').split()))
array.sort()

search_element = int(input('Enter the number you want to search: '))

left_half = 0
right_half = len(array) -1 
found = False

while left_half <= right_half:
    mid_element = (left_half + right_half) // 2
    if array[mid_element] == search_element:
        print(f'Element found at index 02{mid_element}')
        found = True
        break
    elif array[mid_element] < search_element:
        left_half = mid_element + 1
    else:
        right_half = mid_element - 1

if not found:
    print('Element not found ')