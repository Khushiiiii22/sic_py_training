''' You're given:

An array of n integers.
You need to split the array into two parts of size x and y such that x + y = n.
For a value p (where 1 ≤ p ≤ 1000000), the condition must be:
All x elements > p
All y elements < p
Your task is to count how many valid p values satisfy this condition. '''

n , x , y = map(int,input().split())
array = list(map(int,input().split()))

array.sort()
print(array)


if array[n - x] > array[y - 1]:
    # p can be from arr[y-1]+1 to arr[n-x]
    result = array[n - x] - array[y - 1]
else:
    result = 0

print(result)


    

