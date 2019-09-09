# create a set
# find nums not included
def findDisappearedNumbers(self, nums):
	res = []
	numset = set(nums)
	for num in range(1, len(nums) + 1):
		if num not in numset:
			res.append(num)
	return res