A = 10
B = 11
K = 5

C=B-A
if A%K == 0 and B%K == 0 and A!=0:
    if A==B :
        ANS=1
    if A!=B:    
        ANS=(C//K)+2
if A%K == 0 and B%K == 0 and A==0: 
     if A==B :
        ANS=0
     if A!=B:    
        ANS=(C//K)+1  
if A%K == 0 and B%K != 0:
    ANS=(C//K)+1
if A%K != 0 and B%K == 0:
    ANS=(C//K)+1 
if A%K != 0 and B%K != 0:
    for i in range(1,K):
        A=A+1
        C=B-A

        if A%K == 0 and B%K != 0:
          ANS=(C//K)+1
          break
        if A%K != 0 and B%K != 0:
          ANS=0
        
print(ANS)      