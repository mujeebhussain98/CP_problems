# Write the function isFactor(f, n) that takes 
# two int values f and n, and returns True 
# if f is a factor of n, and False otherwise. 
# Note that every integer is a factor of 0.



def fun_isfactor(f, n):
	if f == 0:
		if n == 0:
			return True
		else:
			return False
	else:
		return n%f == 0 # replace with your solution
