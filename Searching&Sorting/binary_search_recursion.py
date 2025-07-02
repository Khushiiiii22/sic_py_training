# Do Binary search using Recursive function


def Binary_search(array,target):
    left_half = 0
    right_half = len(array) - 1

    while left_half <= right_half:
        mid_element = (left_half + right_half) // 2
        if array[mid_element] == target:
            return mid_element
        elif array[mid_element] < target:
            left_half = mid_element + 1
        else:
            right_half = mid_element - 1

array = list(map(int,input('Enter the elements of the list: ').split()))
array.sort()

search_element = int(input('Enter the number you want to search: '))

result = Binary_search(array,search_element)
if result != -1:
    print(f'Element found at index {result}')
else:
    print('Element not found')