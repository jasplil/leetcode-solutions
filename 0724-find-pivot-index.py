# total_sum - left_sum - current_num == left_sum
def pivotIndex(self, nums):
	total = sum(nums)
	left_sum = 0
	for i, num in enumerate(nums):
		if left_sum == (total - left_sum - num):
			return i
		left_sum += num
	return -1