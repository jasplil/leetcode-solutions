# swap order of the element at the end

class Solution:
	def removeElement(self, nums, val):
		i, count = 0, len(nums) - 1
		while i <= count:
			if nums[i] == val:
				nums[i], nums[count] = nums[count], nums[i]
				count -= 1
			else:
				i += 1
		return count + 1
