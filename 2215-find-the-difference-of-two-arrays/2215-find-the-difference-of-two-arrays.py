class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l=[]
        l1,l2=[],[]
        for i in nums1:
            if i not in nums2:
                l1.append(i)
        for i in nums2:
            if i not in nums1:
                l2.append(i)
        l.append(list(set(l1)))
        l.append(list(set(l2)))
        return l