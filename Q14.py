#replace the element in the array with maxi  and min elements
#test case:0
#13 2 67 20 68

list=list(map(int,input().split()))
max=0
min=0
for i in range(0,len(list)):
    if(list[i]>max):
        max=list[i]
    if(list[i<min]):
        min=list[i]
print(max)
print(min)
for i in range(0,len(list)):
    avg=(max+min)//2
    list[i]=avg
print(list)
