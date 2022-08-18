a=int(input("enter the number"))
i=0
sum=0
n=a
while a>0:
    i=a%10
    sum=sum+i
    a//=10
    print(sum)
if n%sum==0:
    print("H")
else:
    print("N")
    