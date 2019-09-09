def majorityElement(self, nums)
	index, count = 0, 1
	for i in range(1, len(nums)):
		if nums[index] = nums[i]:
			count += 1
		else: 
			count -= 1
			if count == 0:
				count = 1
				index = i
	return nums[index]
