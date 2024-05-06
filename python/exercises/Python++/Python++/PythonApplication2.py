def hiluk(m,k):
    c=0
    while(m>=k):
        m=m-k
        c=c+1
    print(c)
    print(m)
    
num1=int(input("enter first number : "))
num2=int(input("enter second number : "))
hiluk(num1,num2)



# def deviders(n):
#     hn=n//2+1
#     i=2
#     while(i<hn):
#         if(n%i==0):
#             print(i,end= " ")
#         i+=1
#     print()
# deviders(100)


def IsPrimary(n):
    hn=n//2+1
    i=2
    while(i<hn):
        if(n%i==0):
            break
        i+=1
    if(i==hn):
            print("Yes")
    else:
      
     print("No")
IsPrimary(345678987654356)
