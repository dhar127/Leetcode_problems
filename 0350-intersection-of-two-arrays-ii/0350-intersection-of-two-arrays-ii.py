class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        nums2_counter = Counter(nums2)
      #  print(nums2_counter)
        for num in nums1:
            if num in nums2_counter and nums2_counter[num] > 0:
                common.append(num)
                nums2_counter[num] -= 1
        return common