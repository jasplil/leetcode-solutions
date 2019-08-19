# if last digit is 9, set the last digit to 0, increment the other digits
# if all digits are 9, set all to 0 and insert 1 in front
# if last digit is not 9, plus one

def plusOne(digits):
	for i in reversed(range(len(digits))):
		if digits[i] == 9:
			digits[i] = 0
		else:
			digits[i] += 1
			return digits

	digits[0] = 1
	digits.append(0)
	return digits