
A=  [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]

a=[0,1]
for i in range(2,len(A)+5):
    if (a[i-1]+a[i-2])<=len(A)+3:
        a.append((a[i-1]+a[i-2]))
    else:
        break
    
indices_befor_the_lake=[]
indices = []
for i in range(len(A)):
    if A[i] == 1:
        indices.append(i)
        indices_befor_the_lake.append((i)+1)
indices_befor_the_lake.append(len(A)+1)  

count_jumps=0
jumps=[]
if len(A)+1 in a:
    count_jumps=1
    
if sum(A)==0 and len(A)+1 not in a:
     count_jumps=-1
   
while indices_befor_the_lake[len(indices_befor_the_lake)-1]!=0 :
    for k in range(len(indices_befor_the_lake)-1,-2,-1):
        for j in range(len(a)-1,0,-1):
            if indices_befor_the_lake[k]==a[j]:
                for l in range(0,len(indices_befor_the_lake)):
                   indices_befor_the_lake[l]=indices_befor_the_lake[l]-a[j]
                count_jumps=count_jumps+1
                jumps.append(a[j])
    
    


if   count_jumps==0:
    count_jumps=-1
             

