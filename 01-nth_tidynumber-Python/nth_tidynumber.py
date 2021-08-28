# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def fun_nth_tidynumber(n):
    c=0
    k=2
    while(c!=n):
        if(isTidy(k)):
            c+=1
        k+=1
    return(k-1)

def isTidy(n):
    while(n!=0):
        digi = n%10
        n//=10
        if(digi<(n%10)):
            return(False)
    return(True)

print(fun_nth_tidynumber(250))