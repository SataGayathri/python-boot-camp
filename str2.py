#ascii values :
#print(ord('A'))
#print(ord('0'))
 #print(ord('l'))
#print(ord('1'))
#print(ord('c'))
#print(ord("<"))
#print(chr(60))""""""

#check how many vowles are there in strigs
 
# check=['a','e','i','o','u']
#count=0
#inp="gayathri"
#for i in inp:
    #if(i in check):
       # count+=1
#print(count)


#write a program to print the lower and upper
#check=['a','e','i','o','u']
##count=0
#i="gayathri"
#input=i.upper()
#for i in input:
    #if(i in check):
      # count+=1
#print(count)


#check=['a','e','i','o','u']
#count=0
#i="gayathri"
#####input=i.lower()
#or i in input:
    #if(i in check):
       #count+=1
#print(count)



#write a program to print the vowels and consonants

'''vowel="aeiou"
consonants="bbjjkhhjdvblaehyjnmwrfbwrwjh"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in consonants):
        c+=1
print(count)
print(c)       ''' 



#print all the level vowles followed by  the consonants
'''vowels="aeiou"
cons='bbccxxccsgjjkkssdbjhuysgdkhdujdmnx'
count=0
c=0
a=""
b=""
i='hello world'
inp=i.lower()
for i in inp:
    if(i in vowels):
        count+=1
        a=a+i
    elif i in cons:
        c+=1
        b=b+i
    else:
        continue
print(count) 
print(c)
print (a+b)   '''
    

#print non repeating characters in a string
''''vowel="aeiou" 
cons='kjdsgyfjbdhbuhbhdxhsk'
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i not in ans):
        ans=ans+i
print(ans) '''



#helloworld123         op:helloworld6
'''vowel="aeiou"
consonants="bbjjkhhjdvblaehyjnmwrfbwrwjh"
check="0123456789"
ans=0
i="hello1234 world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)      
print(ans)'''


#reverse the string
vowel="aeiou"
consonants="bbjjkhhjdvblaehyjnmwrfbwrwjh"
check="0123456789"
ans=0
i="hello1234 world"
inp=i.lower()
for i in inp:
    if(i in check):
        ans+=int(i)      
print(ans) 