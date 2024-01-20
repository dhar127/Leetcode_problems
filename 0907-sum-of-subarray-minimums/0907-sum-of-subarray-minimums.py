class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        arr=[-math.inf]+arr+[-math.inf]
        res=0
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                m=st.pop()
                l=st[-1]
                r=i
                res+=arr[m]*(m-l)*(r-m)
            st.append(i)
        return res%(10**9+7)
        
        