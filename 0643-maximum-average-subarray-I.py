def findMaxAverage(self, nums, k):
	result = total = sum(nums[:k])
  for i in xrange(k, len(nums)):
      total += nums[i] - nums[i-k]
      result = max(result, total)
  return float(result) / k