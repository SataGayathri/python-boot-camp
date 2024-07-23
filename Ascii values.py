#print(ord("A"))
#for i in range(0,128):
    #print(chr(i),end=" ")
 
#output:
#65
#▲ ▼   ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G 
#H I J K L M N O P Q R S T U V W X Y Z [ \ ] ^ _ 
#` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~  

#for i in range(32,128):
   # print(chr(i),end=" ")
 #output:
 # ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B C D E F G H I J K L M N O P Q 
#R S T U V W X Y Z [ \ ] ^ _ ` a b c d e f g h i j k l m n o p q r s t u v w x y z { | } ~  

#ascii values
'''inp=(input())
sum=0
for i in inp:
  if(ord(i)>=48 and ord(i)<=57):
    sum+=int(i)
print(sum)   '''


#write a code to print all the capital letters in the string
'''inp=(input())
for i in inp:
    if(ord(i)>=65 and ord(i)<=90):
        print(i) '''


#remove the all the braces from the algebric expressiinp=(input())
'''inp=str(input())
for i in inp:
  if(ord(i)==40 or ord(i)==41 or ord(i)==91 or ord(i)==93):
    pass
  else:
    print(i,end=" ")
    print()'''


#print(ord("{")) op:123
#print(ord("("))   op:40
#print(ord("["))    op:91
#[(a+b)+c]

#how to print the below code
# ABC=4 
# EFG
'''n=input() #abc
for i in n:
    n=ord(i)+4
    print(chr(n),end="")'''

'''n=input() #abc
for i in n:
    n=ord(i)+4
    if n<=122:
       print(chr(n),end="")
    else:
        print(chr(n-26),end=" ")'''



#input hello -----world
#----hello world "op"
'''inp=input()
count=0
ans=""
for i in inp:
    if(i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans) '''


