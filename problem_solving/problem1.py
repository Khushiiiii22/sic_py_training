# Original String is the right rotated string of the second string given

original_str = input('Enter first word: ')
rotated_str = input('Enter rotated word: ')

temp_str = rotated_str * 2

if original_str in temp_str:
    print(1)
else:
    print(-1)



