class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            key = nums[i]
            if key in hash:
                hash[key]+=1
            else:
                hash[key] = 0
        sorted_keys = [item[0] for item in sorted(hash.items(), key=lambda item: item[1], reverse=True)]        
        return sorted_keys[0:k]