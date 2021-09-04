# isrighttriangle(x1, y1, x2, y2, x3, y3)[5pts]
# Write the function isrighttriangle(x1, y1, x2, y2, x3, y3) that takes 6 int or float values that
# represent the vertices (x1,y1), (x2,y2), and (x3,y3) of a triangle, and returns True if that is
# a right triangle and False otherwise. You may wish to write a helper function,
# distance(x1, y1, x2, y2), which you might call several times. Also, remember to use
# almostEqual (instead of ==) when comparing floats.
import math
def isrighttriangle(x1, y1, x2, y2, x3, y3):
	# your code goes here
    a = abs((distance(x1,y1,x2,y2)))
    b = abs((distance(x1,y1,x3,y3)))
    c = abs((distance(x2,y2,x3,y3)))
    return math.isclose(a, (b+c)) or  math.isclose(b, (a+c)) or math.isclose(c,(b+a))
def distance(x1,y1,x2,y2):
    return ((((y2-y1)**2)+((x2-x1)**2)))