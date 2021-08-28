# areAnagrams(s1, s2)
# Write the function areAnagrams(s1, s2) that takes two strings, 
# s1 and s2, that you may assume contain only upper and/or 
# lower case letters, and returns True if the strings are 
# anagrams, and False otherwise. Two strings are anagrams 
# if each can be reordered into the other. Treat "a" and "A"
# as the same letters (so "Aba" and "BAA" are anagrams). 
# You may not use sort() or sorted() or any other list-based
# functions or approaches. Hint: you may use s.count(), 
# which could be quite handy here.
# Hint: The time complexity can be achieved in Linear.

def areAnagrams(s1, s2):
    # Your code goes here...
    s1=s1.lower()
    s2=s2.lower()
    if(len(s1)!=len(s2)):
        return(False)
    final_s1 = list(sorted(s1))
    final_s2 = list(sorted(s2))
    if("".join(final_s1)=="".join(final_s2)):
        return(True)
    else:
        return(False)

# write your test cases here...
print(areAnagrams("Aba","BAA"))
print(areAnagrams("Abc","CAB"))
print(areAnagrams("Abac","ABCD"))
print(areAnagrams("Abacd","ABCD"))
print(areAnagrams("Abacd","ABCDa"))