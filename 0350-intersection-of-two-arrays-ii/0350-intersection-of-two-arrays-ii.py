class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f=[]
        for i in nums1:
            if i in nums2:
                f.append(i)
                nums2.remove(i)
        return f
                