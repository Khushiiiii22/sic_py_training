# Quick sort

def Quick_sort(array , low , high):
    if low < high:
        pivot_index = partition(array , low , high)
        Quick_sort(array , low , pivot_index-1)
        Quick_sort(array , pivot_index+1 , high)
        
    return array
        
def partition(array , low ,high):
    pivot_index = array[high]
    k = low
    for i in range(low,high):
        if array[i] < pivot_index:
            array[i] , array[k] = array[k] , array[i]
            k += 1
            
            
    array[k] , array[high] = array[high] , array[k]
    return k
    
array = list(map(int,input('Enter the numbers: ').split()))
low = 0
high = len(array)-1

result = Quick_sort(array , low , high)
print(result)