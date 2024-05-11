def max_ele(arr):
    n = len(arr)
    max_ele = -100
    for i in range (len(arr)):
        if max_ele < arr[i]:
            max_ele=arr[i]

    return max_ele

print(max_ele(arr=[1,2,6,7,0,100,3,200,1]))
