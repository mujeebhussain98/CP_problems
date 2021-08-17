# Write the function smallestDifference(a) that takes a list of integers and returns 
# the smallest absolute difference between any two 
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.

def smallestdifference(a):
	# Your code goes here
	if(a==[]):
		return(-1)
	a=list(sorted(a))
	fin_list=[]
	for i in range(len(a)-1):
		fin_list.append(a[i+1]-a[i])
	return(min(fin_list))

print(smallestdifference([1, -3, 71, 68, 17]))