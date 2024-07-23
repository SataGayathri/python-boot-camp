#print the  element particular index by cyclic index
#k=3
 #3 6 8 61 2
#op:4
#------------------
#k=8
#80 70 54 36 72
#op:36
#k=20
#70 54 36 72 76 9999 0089     #k=20,7
# 1 2  3  4  5   6    7       #idx=6 

list=list(map(int,input().split(" ")))
k=int(input())
for i in range(0,len(list)):
    rem=k%(len(list))
print(list[rem])

