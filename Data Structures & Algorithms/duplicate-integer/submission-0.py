class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = set()
        for i in range(len(nums)):
            if nums[i] in nums2:
                return True
            nums2.add(nums[i])
        return False