# find the correspondant x, y in the old matrix for the new matrix
def matrixReshape(self, nums, r, c):
    x = len(nums)
    y = len(nums[0])

    if r*c != x*y:
        return nums

    result = [[0 for _ in range(c)] for _ in range(r)]

    for i in range(x*y):
        result[i//c][i%c] = nums[i//y][i%y]
    return result