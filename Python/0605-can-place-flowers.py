# if n + 1, n - 1 are 0, can plant flowers
def canPlaceFlowers(self. flowbed, n):
	for i in range(len(flowbed)):
		if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
			flowerbed[i] = 1
			n -= 1
		if n <= 0: 
			return True
	return False

