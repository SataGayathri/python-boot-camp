#find the maximum elements in the given list without using max function
#test case:0
#12 23 36 44 45 57
#57
#-----------------------
#test case:1
#56 78 -8 12 34 -99
#78
#-----------------------

list=list(map(int,input().split()))
a=0
for i in range(0,len(list)):
    if(list[i]>a):
     a=list[i]
print(a)