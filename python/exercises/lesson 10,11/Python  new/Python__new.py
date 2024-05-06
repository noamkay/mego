# def Show(a):
#     for r in range(len(a)):#עובר על כל שורה במטריצה
#         for c in range(len(a)):#עובר על כל עמודה במטריצה
#             print(a[r][c], end=" ")
#         print()
# a=[[1,2,3,4,5],
#    [3,4,5,9,8],
#    [7,8,3,2,5],
#    [6,1,4,3,2],
#    [5,4,3,2,1]]

# b=[[1,2,3,3,1],
#    [3,4,5,4,2],
#    [7,8,3,5,3],
#    [6,1,4,9,4],
#    [5,4,3,8,5]]

# for r in range(len(a)):
#     for c in range(len(a)):
#         b[c][len(a)-1-r] = a[r][c]


# Show(a)
# print()
# Show(b)



# def IsSorted(a):
#     for i in range(1, len(a)):
#         if(a[i-1]<a[i]):
#             return False
#     return True

# # ####    MAIN    ####
# a=[4,6,15,21,32,48,59]
# u=IsSorted(a)
# print(u)
# print(IsSorted(a))

# import random

# #מדפיס את כמות האותיות הגדולות במשפט
# s=input("Enter a message : ")
# i=0
# c=0
# while(i<len(s)):
#     if(ord(s[i])>=ord('A') and \
#             ord(s[i])<=ord('Z')):
#         c+=1
#     i+=1
# print(c)

# def bich(arr):
#     for i in range(1,len(arr)-1):
#         if (arr[i]>arr[i-1] and arr[i]>arr[i+1]):
#             print(arr[i])
# a=[2,3,4,3,7,5,8,9,5,4,1,0]
# bich(a)


# def Q(a):
#     i=1
#     while(i<len(a)-1):
#         if(a[i-1]<a[i] and a[i+1]<a[i]):
#             print(a[i])
#             i+=2
#         else:
#             i+=1
# a=[1,2,7,4,5,6,5,4,3,2]
# Q(a)


# def F(a):
#     i=0
#     while(i<len(a)-1 and a[i]<a[i+1]):
#         i+=1
#     if(i==len(a)-1 or i==0):
#         return -1
#     p=i
#     while(i<len(a)-1 and a[i]>a[i+1]):
#         i+=1
#     if(i==len(a)-1):  
#         return p
#     return -1
# a=[1,2,3,4,5,6,5,4,3,2]
# print(F(a))    


# import random
# a=[0]*2000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# print(a)
# for niv in range(0, len(a)-1, 1):
#     for bod in range(niv+1, len(a), 1):
#         if(a[bod]<a[niv]):
#             ezer=a[bod]
#             a[bod]=a[niv]
#             a[niv]=ezer
# print(a)



# import random
# a=[0]*200000
# for i in range(len(a)):
#     a[i]=random.randint(0,100)
# #print(a)
# counters=[0]*101
# for i in range(len(a)):
#     counters[a[i]]+=1
# print()
# print(counters)
# index=0
# for i in range(0, 101, 1):
#     k=0
#     while(k<counters[i]):
#         a[index]=i
#         index+=1
#         k+=1
# print()
# print(a)        



# def Q(a):
#     b=[0]*10
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==a[r][c+1] and a[r][c]==a[r+1][c] and a[r][c]==a[r+1][c+1]):
#                 b[a[r][c]]+=1
#     return b
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# r=Q(a)
# print(r)



#   #2022 sumer A
# def Q14A(a, v):
#     m=0
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     m+=1
#     return m 
# a=[
#     [1,1,3,3,5,8,3,3,5,8],
#     [1,1,8,8,5,5,8,3,5,5],
#     [7,8,8,8,5,5,8,2,5,5],
#     [6,1,1,3,2,2,1,1,2,2],
#     [5,1,1,2,2,2,1,1,2,2]
#     ]
# for i in range(10):
#     print(i, Q14A(a, i))







# def Q14A(a, v):
#     for r in range(len(a)-1):
#         for c in range(len(a[0])-1):
#             if(a[r][c]==v):
#                 if(a[r][c+1]==v and a[r+1][c]==v and a[r+1][c+1]==v):
#                     return True
#     return False  
# a=[
#     [1,2,3,3,5,8],
#     [3,8,8,3,5,5],
#     [7,8,8,2,5,5],
#     [6,1,1,3,2,2],
#     [5,1,1,2,2,2]
#     ]
# for i in range(10):
#     print(Q14A(a, i))



# def Show(a):
#     for r in range(len(a)):
#         for c in range(len(a)):
#             print(a[r][c], end=" ")
#         print()
# a=[
#     [1,2,3,4,5],
#     [3,4,5,9,8],
#     [7,8,3,2,5],
#     [6,1,4,3,2],
#     [5,4,3,2,1]
#     ]
# b=[
#     [1,2,3,3,1],
#     [3,4,5,4,2],
#     [7,8,3,5,3],
#     [6,1,4,9,4],
#     [5,4,3,8,5]
# ]

# #   Rotate right
# # for r in range(len(a)):
# #     for c in range(len(a)):
# #         b[c][len(a)-1-r] = a[r][c]

# #   Rotate left
# for r in range(len(a)):
#     for c in range(len(a)):
#         b[len(a)-1-c][r] = a[r][c]

# Show(a)
# print()
# Show(b)


#NEW DAY 04/4/2024

# def CmpString(s1, s2):
#     l=len(s1)
#     if(len(s1)>len(s2)):
#         l=len(s2)
#     for i in range(l):
#         if(s1[i] != s2[i]):
#            return ord(s1[i]) - ord(s2[i])
#     return len(s1)-len(s2)
   

# print(CmpString("aaa", "bbb"))        
# print(CmpString("ccc", "bbb"))        
# print(CmpString("aaa", "abb"))        
# print(CmpString("axa", "aaaa"))        
# print(CmpString("aaaa", "aaa"))        
# print(CmpString("aaa", "aaaaaaaa"))     





# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     for i in range(len(s1)):
#         for k in range(len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#         if(s1[i]!=s2[k]):
#             return False
#     return True
# print(S1InS2("cea", "casv"))    
# print(S1InS2("cxea", "abcdef"))          
# print(S1InS2("cjea", "abcdef"))          
# print(S1InS2("cea", "cafehb"))    




# def S1InS2(s1, s2):
#     if(len(s1)>len(s2)):
#         return False
#     i=0
#     while(i<len(s1)):
#         k=0
#         while(k<len(s2)):
#             if(s1[i]==s2[k]):
#                 break
#             k+=1
#         if(k==len(s2)):
#             return False
#         i+=1
#     return True
# print(S1InS2("cxea", "abcdef"))          
# print(S1InS2("cjea", "abcdef"))          
# print(S1InS2("ceav", "cae"))           

import random
def Show(a):
    for r in range(len(a)):
        for c in range(len(a)):
            print(a[r][c], end=" ")
        print()
           
r=ord('a')
s=""
for i in range(30):
    c=chr(random.randint(97,106))
    s=s+c
#print(s)
m= [[0 for x in range(10)] for y in range(10)]
for i in range(len(s)-1):
    sh=ord(s[i])-97
    a=ord(s[i+1])-97
    m[sh][a]+=1
rMax=0
cMax=0
for r in range(len(m)):
    for c in range(len(m)):
        if(m[rMax][cMax]<m[r][c]):
            rMax=r
            cMax=c
print(rMax, cMax)
print(chr(rMax+97), chr(cMax+97))
Show(m)    


    
        
    