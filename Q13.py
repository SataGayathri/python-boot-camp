#find the minimum element

list=list(map(int,input().split()))
a=1
for i in range(1,len(list)):
    if(list[i]<a):
     a=list[i]
print(a)