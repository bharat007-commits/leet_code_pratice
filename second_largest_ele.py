def secondLargestElement(arr):
        n=len(arr)
        if n < 2:
            return -1
        else:
            max1 = -10
            max2 = -100
            for i in range(n):
                if arr[i] > max1:
                    max2 = max1
                    max1 = arr[i]
                elif arr[i] > max2 and arr[i] != max1:
                    max2 = arr[i]

## to sort out the array which has same elements
            if max2 == -10:
                return -1
            else:
                return max2
a=[999,999,999,1000]
print(secondLargestElement(a))