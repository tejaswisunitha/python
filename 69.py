n,m=map(int,raw_input().split())
if n>m:
    a=n-m
else:
    a=m-n
if a%2==0:
    print "even"
else:
    print "odd"
