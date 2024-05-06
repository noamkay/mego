import math
def showDeviders(x):
    i=2
    halfx=x//2+1
    for i in range(2,halfx,1):
        if (x%i==0):
            print(i,end="  ")
    
    
num = int(input("Enter a number :"))
showDeviders(num)
print()

    #2  4  5  10
    #50 25 20



def showDeviders(x):
    sqrtx = int(math.sqrt(x))
    for i in range (2,sqrtx,1):
        if (x%i==0):
            print(i,"  ",x//i,end=" ")
    if (sqrtx * sqrtx ==x):
        print(sqrtx)
    else:
        if (x%(i+1)==0):
            print((i+1),x//(i+1))
    print()
    
num = int(input("Enter a number :"))
showDeviders(num)

def IsPrime (x):
    if(x%2==0):
        print("No")
    else:
        sqrtx=int(math.sqrt(x))+1
        i=3
        while(i<sqrtx):
            if (x %i==0):
                print("No")
                break
            i+=2
        if(i>=sqrtx):
            print("YES")

num = int(input("Enter a number :"))
IsPrime(num)



# def Mul(a, b):
#     r = 0
#     while(a > 0):
#         r = r + b
#         a -= 1
#     return r

# def Hezka(x, y):
#     if(Mul(7, 3) > Mul(2, 8)):
#         print("YYY")
#     else:
#         print("NNNN")

# Hezka(0,0)




# def F(x):
#     r=0
#     i=1
#     #   1  -  2  +  3  -  4  +  5  -  6  +  7  =  4
#     while(i<x):
#         if(i%2==0):
#             r=r-i
#             print(i, " + ", end=" ")
#         else:
#             r=r+i
#             print(i, " - ", end=" ")
#         i+=1
#     if(x%2==0):
#         r=r-x
#     else:
#         r=r+x
#     print(x, " = ", r)
#     return r



# num=int(input("Enter a number : "))
# v=F(num)
# print(F(num))
# #   1 - 2 + 3 - 4 + 5 = 3



# def F(x):
#     r=0
#     i=1
#     while(i<x):
#         r=r+i
#         i+=1
#     return r+i

# for i in range(3, 8):
#     print(F(i))



# def F(x):
#     y=x*x
#     return y

# r=F(3)
# print(r)
# print(F(8))



# import math
# def IsPrime(x):
#     if(x%2==0):
#         print("no")
#     else:
#         sqrtX=int(math.sqrt(x)) + 1
#         i=3
#         while(i<sqrtX):
#             if(x%i==0):
#                 print("no")
#                 break
#             i+=2
#         if(i>=sqrtX):
#             print("YES")
       
# IsPrime(100)        
# IsPrime(101)        
# IsPrime(49)        
# IsPrime(80)        
       


# import math
# def ShowDeviders(x):
#     sqrtX=int(math.sqrt(x))
#     for i in range(2, sqrtX, 1):
#         if(x%i==0):
#             print(i, "  ", x//i, end="  ")
#     if(sqrtX*sqrtX==x):
#         print(sqrtX)
#     else:
#         i+=1
#         if(x%i==0):
#             print(i, x//i)
#     print()

# ####    MAIN    ####

# num=int(input("Enter a number : "))
# ShowDeviders(num)


#   2   4   5   10
#   50  25  20      



#   100     2 4 5 10 20 25 50


# def Mul(a, b):
#     r=0
#     while(a>0):
#         r=r+b
#         a-=1
#     return r
# def Hezka(x, y):
#     t=1
#     while(y>0):
#         t=Mul(t,x)
#         y=y-1
#     return t

# print(Hezka(5,4))
# print(Hezka(10,3))
# print(Hezka(6,2))
# print(Hezka(7,1))


