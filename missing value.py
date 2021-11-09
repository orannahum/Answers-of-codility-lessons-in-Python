#An array A consisting of N different integers is given. 
#The array contains integers in the range [1..(N + 1)], which means that exactly 
#one element is missing.

#Your goal is to find that missing element.

#Write a function:


#that, given an array A, returns the value of the missing element.

#For example, given array A such that:

#  A[0] = 2
#  A[1] = 3
#  A[2] = 1
#  A[3] = 5
#the function should return 4, as it is the missing element.

A=[1,3]
MIN=min(A)
MISS_VALUE=[]
for i in range (0,len(A)):
    if MIN+i not in A:
        MISS_VALUE=MIN+i
        break
    
    