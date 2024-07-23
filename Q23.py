#write a program to print all the prime numbers in given range
#a=int(input("enter the value of a:"))
#b=int(input("enter the value of b:"))
#for i in range(a,b+1):
   # for j in range(2,i):
       # if i%j==0: 
            #break
#else:
   # print(i)


    #print the leap year by the range
#n=int(input())
#for i in range(1,n+1):
    #if(n%400==0):
       # print("leap year")
#else:
   # print("not a leap year")


n=int(input())
for i in range(2000,2025):
    if i%4==0 and i%100!=0:
        print(i)