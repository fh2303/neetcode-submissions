class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # Step 1: Count frequencies
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Create buckets where index = frequency
        # Example: if nums has 6 elements, max frequency is 6. 
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Populate buckets
        for num, freq in count.items():
            buckets[freq].append(num)
            
        # Step 4: Collect top k elements from right to left
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result