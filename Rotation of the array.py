#An array A consisting of N integers is given. Rotation of the array means that each 
#element is shifted right by one index, and the last element of the array is moved to the 
#first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] 
#(elements are shifted right by one index and 6 is moved to the first place).
#The goal is to rotate array A K times; that is, each e
#lement of A will be shifted to the right K times.
#Write a function:
#def solution(A, K)
#that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
#For example, given
#    A = [3, 8, 9, 7, 6]
#    K = 3
#the function should return [9, 7, 6, 3, 8]. Three rotations were made:
#For another example, given
#    A = [0, 0, 0]
#    K = 1
#the function should return [0, 0, 0]
#Given
#    A = [1, 2, 3, 4]
#    K = 4
#the function should return [1, 2, 3, 4]

def solution(A, K):
    NEW_A=[0] * (len(A))
    if K>len(A) and len(A) != 0:
        K=K%len(A)

    if len(A) != 0:
        for i in range(0,len(A)-K):
            NEW_A[i+K]=A[i]
            
        for j in range(0,K):
            NEW_A[j]=A[len(A)+j-K]

    if len(A) == 0 :
        NEW_A=A
    return(NEW_A) 