#"7 Q your given with a coma separated by natural numbers 1to 10 and print that even numbers""""""
#my_list=list(map(int,input().split(",")))
#for i in range (1,10+1):
 #if(i%2==0):
    #print(i)

#my_list=list(map(int,input().split(",")))
# i in range (1,len(my_list),2):
 # print(i)

#my_list=list(map(int,input().split(",")))
#count=0
#for i in range (1,len(my_list),2):
# count+=1
#print(count)

#7.3 give with a space sparated integer list and find num of even and odd elements in given list
my_list=list(map(int,input().split(",")))
even=0
odd=0
for i in range(0,len(my_list)):
 if(my_list[i]%2==0):
    even+=1
 else:
    odd+1
print(odd)
print(even)