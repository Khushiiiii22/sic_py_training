# Remove the duplicates in a list of size n

list = [2 , 4 , 5 , 1 , 4 , 2 , 6 , 6 , 1]
duplicate = []

for num in list:
    if num not in duplicate:
        duplicate.append(num)

print('List after removing duplicates: ',duplicate)

        