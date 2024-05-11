def selection_sort(arr):
    n= len(arr)
    # we are taking n-1 becuase if we sort n-1 elements last element by default will be sorted.
    for i in range(n-1):
        min_index =i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        ## swaping
        arr[i],arr[min_index]=arr[min_index],arr[i]

    return arr

