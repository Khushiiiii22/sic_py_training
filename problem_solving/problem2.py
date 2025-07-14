# Find the total number of units of memory allocated/deallocated by the server 1 after processing al the requests.

# Memory allocated(denoted by a positive integer)
# Memory deallocation(denoted by a negative integer)


total = 0
N = int(input('Enter Number of Requests: '))

requests = list(map(int,input('Enter the requests with space: ').split()))

# If 1st request goes to server one that is index 0 then (0,2,4): even placed will go to server 1

for i in range(0,N+1,2):
    total += requests[i]

print('Total number of units of memory by server 1: ',total)



