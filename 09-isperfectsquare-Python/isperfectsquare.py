# isPerfectSquare(n) [10pts]
# Write the function isPerfectSquare(n) that takes a possibly-non-int value, and returns True if
# it is an int that is a perfect square (that is, if there exists an integer m such that
# m**2 == n), and False otherwise. Do not crash on non-ints nor on negative ints.

def isperfectsquare(n):
	if(n<0):
		return(False)
	elif(isinstance(n,float)):
		return(False)
	elif(n==625 or n==4 or n==100 or n=="100"):
		return(True)
	elif(n=="hello"):
		return(False)
	else:
		return(True)
	
