#For a given array A of N integers and a sequence S of N integers from the set {−1, 1}, we define val(A, S) as follows:
#val(A, S) = |sum{ A[i]*S[i] for i = 0..N−1 }|
#(Assume that the sum of zero elements equals zero.)
#For a given array A, we are looking for such a sequence S that minimizes val(A,S).

#Write a function:
#that, given an array A of N integers, computes the minimum value of val(A,S) from all possible values of val(A,S) for all possible sequences S of N integers from the set {−1, 1}.
#For example, given array:
#  A[0] =  1
#  A[1] =  5
#  A[2] =  2
#  A[3] = -2
#your function should return 0, since for S = [−1, 1, −1, 1], val(A, S) = 0, which is the minimum possible value.
#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [0..20,000];
#each element of array A is an integer within the range [−100..100].

def solution(A):
    SUM_MIN_SLICE=abs(sum(A))
    NEW_A=A
    if len(A)==0:
        return(0)
    if len(A)==1:
        return(A[0])
        
    for i in range(2**len(A)):
        BINARY_MULTIPLAY_str=str(bin(i)[2:])
        BINARY_MULTIPLAY_arr=[0]*len(BINARY_MULTIPLAY_str)
        for k in range(0,len(BINARY_MULTIPLAY_str)) :
            if BINARY_MULTIPLAY_str[k]=='0':
                BINARY_MULTIPLAY_arr[k]=-1
            else:
                BINARY_MULTIPLAY_arr[k]=1 
            NEW_A[k]= BINARY_MULTIPLAY_arr[k]*A[k] 
            if abs(sum(NEW_A))<SUM_MIN_SLICE:
                SUM_MIN_SLICE=abs(sum(NEW_A))
    return(SUM_MIN_SLICE)            