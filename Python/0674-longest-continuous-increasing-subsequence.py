# 动态规划
def findLengthOfLCIS(self, nums):
	result, count = 1, 1
	for i in range(1, len(nums)):
		if nums[i] > nums[i - 1]:
			count += 1
			result = max(result, count)
		else:
			count = 1
	return result

