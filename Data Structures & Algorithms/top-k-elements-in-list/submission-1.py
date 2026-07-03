class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
                continue
            hashmap[n] = 1
        sorted_ = sorted(hashmap, key=hashmap.get, reverse=True)[:k]
        return sorted_