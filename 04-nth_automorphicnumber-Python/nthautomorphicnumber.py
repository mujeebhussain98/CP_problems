# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.

def nthautomorphicnumbers(n):
	# Your code goes here
	c=1
	k=1
	while(c!=n):
		if(isAutomorphic(k)):
			c+=1
		k+=1
	return(k-1)

def isAutomorphic(n):
    p=pow(n,2)
    while(n>0):
        if(n%10!=p%10):
            return(False)
        n//=10
        p//=10
    return(True)