# create a merge sort using Recursion
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        print('beginning: ', arr)
        print('left is: ', left)
        print('right is: ', right)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i += 1
                print('first loop(left):', arr)
            else:
                arr[k]=right[j]
                j += 1
                print('first loop(right):', arr)
            k += 1           
            
        print('value for i: ', i, ' value for len(left) is: ', len(left))    
        while i < len(left):
            arr[k]=left[i]
            i += 1
            k += 1
            print('Output second loop: ', arr)
            
        while j < len(right):
            arr[k]=right[j]
            j += 1
            k += 1
            print('Output third loop: ', arr)
            
    return arr

# merge_sort algorithm
arr = [5, 1, 8, 3, 6, 9, 2, 4]
print(arr)

merge_sort(arr)
print(arr)

