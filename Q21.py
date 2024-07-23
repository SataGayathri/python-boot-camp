#peak element
#list=list(map(int,input().split()))
#peak=0
#for i in range(1,len(list)-1):
    #if(list[i-1]>list[i] and list[i+1]>list[i]):
       #peak=list[i]
       #break
#print(peak)


#all peak values
#list=list(map(int,input().split()))
#count=0
#for i in range(1,len(list)-1):
    #if list[i]>list[i-1] and list[i]>list[i+1]:
        #count=i
        #break
        #print(list[i],end=" ")

list=list(map(int,input().split()))
count=0
for i in range (1,len(list)-1):
    if list[i]>list[i-1] and list[i]>list[i+1]:
        count=1
if(list[-1]>list[-2] and list[-1]>count):
    count=len(list)-1
print(list[count])