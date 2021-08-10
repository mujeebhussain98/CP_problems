# dicetoorderedhand(a, b, c) [5pts]
# Write the function dicetoorderedhand(a, b, c) that takes 3 dice and
# returns them in a hand, which is a 3-digit integer. However, even if the
# dice are unordered, the resulting hand must be ordered so that the largest
# die is on the left and smallest die is on the right. For example:
# assert(dicetoorderedhand(1,2,3) == 321)
# assert(dicetoorderedhand(6,5,4) == 654)
# assert(dicetoorderedhand(1,4,2) == 421)
# assert(dicetoorderedhand(6,5,6) == 665)
# assert(dicetoorderedhand(2,2,2) == 222)


def dicetoorderedhand(a, b, c):
	# your code goes here
	sum=0
	digit_list=[]
	digit_list.append(a)
	digit_list.append(b)
	digit_list.append(c)
	mid_list = list(reversed(sorted(digit_list)))
	ten_digits_list= list(reversed([10**j for j in range(len(mid_list))]))
	for i in list(zip(mid_list,ten_digits_list)):
		sum += i[0]*i[1]
	return(sum)