def pow(x,n):
    if n<0:
        n=-n
        return pow(1/x,n)
    if x==0 & n >0:
        return 0
    if n==0:
        return 1
    res = 1
    while n > 0:
        if n %2 ==0:
            x=x*x
            n=n/2
        else:
            res = x* res
            n=n-1
    return res


print(pow(3,6))
