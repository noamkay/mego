# a=[
#    [3,5,6,6,9],
#    [3,5,4,1,2],
#    [7,4,5,6,7],
#    [1,2,3,4,0]
# ]
# m=0
# for r in range(len(a)):
#     for c in range(len(a[r])-1):
#         if a[r][c]+1==a[r][c+1]:
#             m+=1
# print(m)
        




# a=[
#     [3,5,7,6,9],
#     [3,5,4,1,2,4,4,5],
#     [7,4,5,6,7,3],
#     [1,2,3],
# ]
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         print(a[r][c], end=" ")
#     print()
       
'''
3 5 7 6 9      
3 5 4 1 2 4 4 5
7 4 5 6 7 3
1 2 3
'''


# a=[45,102,674,19,876,45]
# #a=[102,674,19,876,45,45]
# temp=a[0]
# for i in range(1, len(a)):
#     a[i-1]=a[i]
# #a[len(a)-1]=temp    
# a[i]=temp    
# print(a)    




# a=[-456,-102,-67834,-19,-876,-45]
# #a=[6,2,8,9,8,5]
# max=a[0]
# for i in range(len(a)):
#     if(max<a[i]):
#         max=a[i]
# print(max)    






# a=[456,102,67834,1009,876,45]
# #a=[6,2,8,9,8,5]
# for i in range(len(a)):
#     max=0
#     while(a[i]>0):
#         if(max<a[i]%10):
#             max=a[i]%10
#         a[i]=a[i]//10
#     a[i]=max
# print(a)    




# a=[456,102,67834,1009,876,45]
# #a=[15,3,28,10,21,9]
# for i in range(len(a)):
#     sum=0
#     while(a[i]>0):
#         sum=sum+a[i]%10
#         a[i]=a[i]//10
#     a[i]=sum
# print(a)    





# a=[456,102,67834,1009,876,45]
# #a=[4,1,6,9,8,4]
# for i in range(len(a)):
#     while(a[i]>9):
#         a[i]=a[i]//10
# print(a)    




# a=[456,12,67834,9,876,45]
# #a=[3,2,5,1,3,2]
# for i in range(len(a)):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)    



# def IntToString(n):
#     s=""
#     while(n>0):
#         t=chr((n%10)+48)
#         s=t+s
#         n=n//10
#     return s
   
# y=6834
# x=IntToString(y)
# x=x+"fdhf"
# print(x)

# x=6834
# y=str(x)
# y=y+"***"
# print(y)



# def StringToInt(s): #   s="6824"
#     num=0
#     ord0=ord('0')   #   48
#     for i in range(len(s)):
#         num = num*10 + ord(s[i])-ord0
#     return num
# qqq=input("Enter a number : ")
# qqq="4561"
# n = StringToInt(qqq)
# n=n+1
# print(n)

# #   3 6 2   ====>   362
# #   0*10 + 3    3
# #   3*10 + 6    36
# #   36*10+ 2    362


# r=9
# t=r+1
# while(r>0):
#     for s in range(r, 0, -1):
#         print("*", end=" ")
#     s=r
#     while(s<t):
#         print(r, end=" ")
#         s+=1
#     # for s in range(r, t, 1):    
#     #     print(r, end=" ")
#     print()
#     r-=1

# '''
# *****5
# ****44
# ***333
# **2222
# *11111

# '''



# def Show(n):
#     for r in range(n):    #   (0, n, 1)
#         for c in range(-1, r, 1):
#             print("*", end=" ")
#         print()
# Show(4)
# Show(5)


# def Mul(a, b):
#     if(a<b):
#         r=0
#         while(a>0):
#             r=r+b
#             a-=1
#     else:
#         r=0
#         while(b>0):
#             r=r+a
#             b-=1
#     return r

# print(Mul(5, 6))
# print(Mul(5, 6))


# d=0
# r=1
# while(r<5):
#     d=d+r
#     print(d, r)
#     r+=1
# print((d+r), r)
# #   d=0     1   3   6   10  
# #   r=1     2   3   4   5  

# #                   1   1
# #                   3   2
# #                   3   2
# #                   10  4
# #                   10  5



print("He" + "l" * 2 + "o" + " Python " + str(7.2 / 2) + "." + str(3))

rounds_and_winners ="\nrounds winner \nround 1 \tdana \nround 2 \tnoam \nround 3 dana"
print(rounds_and_winners)