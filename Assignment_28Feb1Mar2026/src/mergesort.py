def merge (arr1,arr2):
    result=[]
    len_1 = len(arr1)
    len_2 = len(arr2)
    i=0
    j=0
    while i < len_1 and j <len_2:
        if arr1[i] < arr2[j]:
          result.append(arr1[i])
          i+=1          
        elif arr2[j]<arr1[i]:
          result.append(arr2[j])
          j+=1
        else:
            result.append(arr1[i])
            result.append(arr2[j])
            i+=1
            j+=1
    # Add remaining elements of arr1
    while i < len_1:
        result.append(arr1[i])
        i+=1
    # Add remaining elements of arr2
    while j < len_2:
        result.append(arr2[j])
        j+=1
    return result
def merge_sort(arr):
    
    if len(arr) <= 1:
        return arr    
    mid_index = len(arr) // 2
    # Split the list into two halves
    arr1 = arr[:mid_index]
    arr2 = arr[mid_index:]    
    arr1 = merge_sort(arr1)
    arr2 =merge_sort(arr2) 
    return merge(arr1, arr2)

#merge_sort([1,2,-1,3,10,5,4,0])
    