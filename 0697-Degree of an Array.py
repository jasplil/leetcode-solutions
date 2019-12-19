# set two dictionaries from left and right to see how many times the number occures from both sides

import collections

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        left, right = {}, {}
        for i, num in enumerate(nums):
            left.setdefault(num, i)
            right[num] = i
        degree = max(counts.values())
        res = float("inf")
        for num in counts.keys():
            if counts[num] == degree:
                res = min(res, right[num] - left[num] + 1)
        return res