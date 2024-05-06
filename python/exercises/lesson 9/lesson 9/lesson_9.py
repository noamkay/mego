def mirror(m):
    left=0
    right=len(m)-1
    while(left<right):
        ezer=m[left]
        m[left]=m[right]
        m[right]=ezer
        right-=1
        left+=1
a=[1,2,3,4,5,6,7,8]
print(a)
mirror(a)
print(a)

# a=[10,3,67,20,31,40,57,62,70,89,77,6,78]
# #a=[10,20,70,40,57,62,31,89,77]
# #a=[10,20,70,40,62,57,31,89,77]
# right=len(a)-1
# left=0
# while(left<len(a) and a[left]%2==0):
#     left+=1
# if(left<len(a)-1):
#     while(left<right and a[right]%2==1):
#         right-=1
#     while(left<right):
#         if(a[right]%2==0 and a[left]%2==1):
#             ezer=a[left]
#             a[left]=a[right]
#             a[right]=ezer
#             right-=1
#             left+=1
#         else:
#             if(a[right]%2==1):
#                 right-=1
#             else:
#                 if(a[left]%2==0):
#                     left+=1
# print(a)
   
# import random
# a=[0]*1000
# a[0]=2
# for i in range(1,len(a)):
#     a[i]=a[i-1]+random.randint(1,6)
#     x=6666
#     low=0
#     up=len(a)-1
#     middle=(low+up)//2
#     while(low<up):
#         if(x==a[middle]):
#             print(middle)
#             break
        
# import random
# def BinariSearch(a):
#     low=0
#     up=len(a)-1
#     while(low<up):
#         mid=(low+up)//2
#         if(x==a[mid]):
#             return mid
#         if(x<a[mid]):
#             up=mid-1
#         else:
#             low=mid+1
#     return -1
   
# a=[0]*10000
# a[0]=2
# for i in range(1,len(a)):
#     a[i]=a[i-1]+random.randint(1,6)
# print(a)    
# x=int(input("Enter a number : "))
# print(BinariSearch(a))    




# import random
# def BinariSearch(a, x):
#     low=0
#     up=len(a)-1
#     while(low<=up):
#         mid=(low+up)//2
#         if(x==a[mid]):
#             return mid
#         if(x<a[mid]):
#             up=mid-1
#         else:
#             low=mid+1
#     return -1
# def Search(a, x):
#     for i in range(len(a)):
#         if(a[i]==x):
#             return i
#     return -1
   
# a=[0]*100000
# a[0]=2
# for i in range(1,len(a)):
#     a[i]=a[i-1]+random.randint(1,6)
# print(a)    
# y=int(input("Enter a number : "))
# print(BinariSearch(a, y))  


# a=[456,12,67834,9,876,45]
# for i in range(len(a)):
#     c=0
#     while(a[i]>0):
#         c+=1
#         a[i]=a[i]//10
#     a[i]=c
# print(a)
