# r=26
# st=1
# while(r>0):
#     sp=r-1
#     while(sp>0):
#         print(" ",end=" ")
#         sp=sp-1
#     ko=st
#     while(ko>0):
#         print("*",end=" ")
#         ko-=1
#     print()
#     r-=1
#     st+=1
# print("the end")




# a=21
# b=5
# c=a//b # c = 4
# d=a%b  # d = 1
# e=a/b  # e = 4.2



# r=6231
# t=0
# while(r>0):
#     t=t+(r%10)
#     r=r//10
#     print(r,t)

# #טבלת מעקב
# # r = 6231  623  62  6  0
# # t = 0     1    4   6  12

# r=int(input("enter a number :"))
# if(r>0):
# t=0
#     while(r>0):
#         t=t+(r%10)
#         r=r//10
#         print(r,t)
#     print(r,t)
# else:
#     print("wrong input")




# r=int(input("enter a number :"))    
# while(r<1):
#     r=int(input("error enter again : "))
# t=0
# while(r>0):
#     t=t+(r%10)
#     r=r//10
#     print(r,t)
# print(r,t)

 

# num=int(input("enter a number :"))    
# t=0
# while(num>0):
#     t=t*10+num%10
#     num=num//10
# print(t)
# #טבלת מעקב כשהוזן הערך 1234
# #num = 1234  123  12  1  0
# #t =    0    432  43  4  1

# # #  0  1  2  3  4  5     index
# a=[33,11,66,55,77,88]
# i=0
# while(i<6):
#     print(a[i])
#     i+=1




# #  0  1  2  3  4  5     index
# a=[33,11,66,55,77,22]
# m=a[0]
# i=1
# while(i<6):
#     if(m<a[i]):
#         m=a[i]
#     print(m)
#     i+=1
# print("the end")

# #טבלת מעקב
# # m = 33  66  77
# # i = 1  2  3  4  5  6
# # screen = 33  66  66  77  77  the end


print("world")
