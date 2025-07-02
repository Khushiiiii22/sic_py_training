# Orange partition program

n = int(input('Enter the number of oranges'))
oranges = list(map(int,input('Enter the size of oranges: ').split ()))


k = 0
pivot = oranges[-1]

for i in range(n-1):
    if oranges[i] <= pivot:
        oranges[i] , oranges[k] = oranges[k] , oranges[i]
        k += 1

oranges[k] , pivot = pivot , oranges[k]

print(' '.join(map(str, oranges))) #to join and print
