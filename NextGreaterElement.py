from typing import List

## basic funda is stack banao upar se niche badte karam mai and and start making stack from the right
## most side of the array.


class Solution():
    def ciruclarNextGreaterElement(self, nums:List[int])-> List[int]:
        n=len(nums)
        st=[]
        nge =[-1]*n
        for i in range(2*n-1,-1,-1):
            while st and st[-1]<= nums[i%n]:
                st.pop()

            if i<n :
                if st:
                    nge[i]=st[-1]
            st.append(nums[i%n])
        return nge

    def nonCircularNextGreaterElement(self,nums=List[int])-> List[int]:
        n=len(nums)
        nge= [-1]*n
        st=[]
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums[i]:
                st.pop()
            if i<n:
                if st:
                    nge[i]=st[-1]
            st.append(nums[i])
        return nge

if __name__ == '__main__':
    obj = Solution()
    v = [12,2,4,6]
    # res = obj.ciruclarNextGreaterElement(v)
    # print("The next greater elements are")
    # print(*res)
    res=obj.nonCircularNextGreaterElement(v)
    print("The next greater elements are")
    print(*res)


