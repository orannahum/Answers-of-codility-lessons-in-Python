#
#A binary gap within a positive integer N is any maximal sequence of consecutive zeros
#that is surrounded by ones at both ends in the binary representation of N.

#For example, number 9 has binary representation 1001 and contains a binary gap of length 2. 
#The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4
#and one of length 3. The number 20 has binary representation 10100 and contains one binary gap 
#of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 
#has binary representation 100000 and has no binary gaps.
#Example test:   1041 (binary = 10000010001)
#output is : 3

#Example test:   15 (binary = 1111)
#output is : 0

#Example test:   32 (binaery =100000)
#output is 100000

def solution(N):
    # write your code in Python 3.6
    
    most_of_ZEROS=0
    Z=0
    N=bin(N)[2:]
    for k in range(1,len(N)+1):
        if N[k-1] == '0' and N[k-2] == '1':
            Z=1
            for j in range(0,len(N)-k):
                if N[k+j-1] == '0' and   N[k+j] == '0':
                    Z=Z+1
                if N[k+j-1] == '0' and   N[k+j] == '1': 
                    if most_of_ZEROS < Z:
                       most_of_ZEROS=Z 
                    Z=0
                    break
    return(most_of_ZEROS)                
                
            
    
