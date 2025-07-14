#Hackerrank Greedy Florist problem


n_k = input().strip().split()
n = int(n_k[0])
k = int(n_k[1])
c = list(map(int, input().strip().split()))

c.sort(reverse = True)

total_cost = 0

for i in range(len(c)):
    multiplier = i // k + 1
    total_cost += multiplier * c[i]

print(total_cost)
    
     