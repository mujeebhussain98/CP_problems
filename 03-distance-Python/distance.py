# Write the function fun_distance(x1, y1, x2, y2) 
# that takes four int values x1, y1, x2, y2 
# that represent the two points (x1, y1) and (x2, y2), 
# and returns the distance between those points as a int.

import math
def fun_distance(x1, y1, x2, y2):
	# your code goes here
	z1=pow((x2-x1),2)
	z2=pow((y2-y1),2)
	final = math.sqrt(z1+z2)
	ans = "%d" %final
	return(int(ans))