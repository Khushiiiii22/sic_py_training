'''
You are given heights of boys and girls. You need to arrange them in a line such that:
The total order is non-decreasing in height.
No two boys or two girls are adjacent.
✔️ You need to output "YES" if such an arrangement is possible, otherwise "NO".
'''

# Read input
t, n = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

def is_valid(first, second):
    result = []
    for i in range(n):
        result.append(first[i])
        result.append(second[i])
    # Check non-decreasing order
    for i in range(1, len(result)):
        if result[i] < result[i-1]:
            return False
    return True

# Try both arrangements
if is_valid(boys, girls) or is_valid(girls, boys):
    print("YES")
else:
    print("NO")




