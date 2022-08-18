
# i=0
# while i<=10:
#     if i%2==0:
#         print(i)
#     # else:
#     #     print(i)
#     i+=1


# i=0
# while i<=10:
#     if i%2!=0:
#         print(i)
#     i+=1

# i=0
# while i<=10:
#     # i+=1
#     print(i)
#     i+=1

# i=0
# while i<=10:
#     # if (i**2):
#     print(i,i**2)
#     i+=1

# i=0
# while i<=10:
#     print(i)
#     if i==3:
#         break
#     i+=1

# i=0
# while i<=10:
#     i+=1
#     if i==5:
#         continue
#     print(i)

# i=10
# while i<=300:
#     print(i)
#     i+=10

# i=1  
# while i<=100:
#     if i%7==0:
#         print(i)
#     i+=1

# i=105
# while i>=7:
#     print(i)
#     i-=7

# i=10
# while i>=1:
#     print(i)
#     i-=1

# i=9
# while i>=1:
#     print(i)
#     i-=1

# i=0
# sum=0
# while i<=10:
#     sum=sum+i
#     print(sum)
#     i+=1

# i=0
# sum=0
# while i<=10:
#     if i%2==0:
#         sum=sum+i
#         print(sum)
#     i+=1

# a=int(input("enter the number"))
# i=1
# while i<=10:
#     print(a,"*",i,"=",i*a)
#     i+=1

# a=int(input("enter the number"))
# if a<=100:
#     print(a,"*",1,"=",a*1)
#     print(a,"*",2,"=",a*2)
#     print(a,"*",3,"=",a*3)
#     print(a,"*",4,"=",a*4)
#     print(a,"*",5,"=",a*5)
#     print(a,"*",6,"=",a*6)
#     print(a,"*",7,"=",a*7)
#     print(a,"*",8,"=",a*8)
#     print(a,"*",9,"=",a*9)
#     print(a,"*",10,"=",a*10)

# a=int(input("enter the number"))
# i=1
# c=0
# while i<=a:
#     if a%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("prime no")
# else:
#     print("not")

# i=1
# c=0
# while i<=100:
#     if c%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("prime")
# else:
#     print("not")

# a=[2,3,4,5,6,7,8,9,11]
# i=1
# c=0
# b=0
# while i<len(a):
#     if a[i]%i==0:
#         c+=1
#         # b.append(c)
#     i+=1
# if c==2:
#     print("prime")
# else:
#     print("not")

# i=1
# sum=0
# while i<=20:
#     sum=sum+i
#     print(sum)
#     i+=1

# a=int(input("enter the number"))
# i=1
# c=0
# while i<=a:
#     if a%i==0:
#         c+=1
#     i+=1
# if c==2:
#     print("p")
# else:
#     print("n")

# i=10
# while i>=1:
#     print(i)
#     i-=1

# i=int(input("enter the number"))
# rev=0
# while i>0:
#     rev=(rev*10)+i%10
#     i=i//10
# print("rev",rev)

# i=1
# while i<=100:
#     j=1
#     count=0
#     while j<=i:
#         if i%j==0:
#             count+=1
#         j+=1
#     if count==2:
#         print("p",i)
#     else:
#         print("not",i)
#     i+=1

# a=int(input("enter the number"))
# i=0
# rev=0
# while a>0:
#     i= {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"eine"}:
#     if i<len(i):
#         rev=(rev*10)+a%10
#         a=a//10
# print(rev[i])

# a=int(input("enter the number"))
# i=1
# while a>0:
#     i=i*a
#     a-=1
# print(i)

# a=int(input("enter the number"))
# b=a
# sum=0
# while a>0:
#     sum=sum+(a%10)*(a%10)*(a%10)
#     a=a//10
# if b==sum:
#     print("A")
# else:
#     print("not")

num=int(input("enter the number"))
sum=0
i=0
while num>0:
    rev=num%10
    num=num//10
    sum=sum+rev*(2**i)
    i=i+1
print("decimal",sum)



