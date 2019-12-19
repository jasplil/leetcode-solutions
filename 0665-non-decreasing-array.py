# [2, 4, 2, 6]
# [3, 4, 2, 6]
def checkPossibiltiy(self, nums):
	for i in range(1, len(nums)):
    if prev > nums[i]:
      if modified:
          return False
      if i-2 < 0 or nums[i-2] <= nums[i]:
          prev = nums[i]                   
      else:                  
          prev = nums[i-1]
      modified = True
    else:
        prev = nums[i]
	return True