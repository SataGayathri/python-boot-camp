#Gcd of two numbers
#Eucliden algorithm
#b=int(input("enter 2nd number:"))
#while b!=0:
    #,b=b,a%b
#print("GCD of 2 num is:",a)


#print LCM
#a=int(input())
#b=int(input())
#c=a*b
#while b!=0:
    #a,b=b,a*b
    #GCD=a
#print("LCM of 2 num is:",a)
#LCM=c//GCD
#print(LCM)


#print prime number or not
a=int(input("enter a number:"))
r=a**0.5
count=0
if a==1:
    print("not a prime number")
elif a==2:
    print("prime number")
for i in range(2,int(r+1)):
     if a%i==0: 
        count=1
        break
if count==0:
    print("prime number")
else:
    print("not prime number")