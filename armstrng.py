num=int(raw_input())
length=len(str(num))
sum=0
temp=num
while(temp!=0):
  sum=sum+((temp%10)**length)
  temp=temp//10
if sum==num:
   print("yes")
else:
   print("no")
