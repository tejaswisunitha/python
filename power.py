def power(a,b):
        if a==0: return 0
        elif b==0: return 1
        elif b==1: return a
        elif b%2 == 0:
                res_even = power(a,b/2)
                return res_even*res_even
        else :
                b=(b-1)/2
                res_odd= power(a,b)
                return a*res_odd*res_odd
pow = power(2,3)
print(pow)
