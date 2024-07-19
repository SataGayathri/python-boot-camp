#given  n space separated integer list find the average of elements present in the index
#list=list(map(int,input().split(" ")))
#even=0
#sum=0
#for i in range(0,len(list)):
   # if(i%2==0):
   #     even+=1
        #sum=sum+list[i]
     #   avg=sum//even
#print(avg)   



my_list=list(map(int,input().split()))
sum=0
count=0
n=len(my_list)
for i in range(len(my_list)):
    if(i%2==0):
        sum+=my_list[i]
        count+=1
        print(sum/count)