# a=int(input("enter the number"))
# i=1
# s=0
# b=a
# while a>0:
#     a=a%10
#     s=s+i
#     # a=a//10
# if b==s:
#     print("perfect number")
# else:
#     print("not")
#     i=i+1

a=int(input("enter the number"))
sum=0
i=1
while a>i:
    if a%i==0:
        sum=sum+i
        # i+=1
        a//=10
    i+=1
if sum==a:
    print("perfect")
else:
    print("not")
    # i+=1
