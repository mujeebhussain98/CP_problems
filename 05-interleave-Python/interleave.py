# Write the function interleave(s1, s2) that takes two strings, s1 and s2, 
# and interleaves their characters starting with the first character in s1. 
# For example, interleave('pto', 'yhn') would return the string "python". 
# If one string is longer than the other, concatenate the rest of the remaining 
# string onto the end of the new string. For example ('a#', 'cD!f2') would return 
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.


def fun_interleave(s1,s2):
	if(len(s1)==len(s2)):
		st=""
		li=list(zip(s1,s2))
		for i in li:
			st+=(i[0]+i[1])
		return(st)
	elif(len(s1)<len(s2)):
		st1=""
		diff = len(s2)-len(s1)
		s1 = s1+" "*diff
		li1 = list(zip(s1,s2))
		for i in li1:
			st1+=(i[0]+i[1])
		p = st1.split()
		return("".join(p))
	elif(len(s1)>len(s2)):
		st2=""
		diff1 = len(s1)-len(s2)
		s2 = s2+"@"*diff1
		li2 = list(zip(s1,s2))
		for i in li2:
			st2+=(i[0]+i[1])
		q=st2.split("@")
		return("".join(q))
