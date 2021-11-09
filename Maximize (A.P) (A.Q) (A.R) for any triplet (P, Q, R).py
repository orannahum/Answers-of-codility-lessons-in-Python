#A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
#For example, array A such that:
#  A[0] = -3
#  A[1] = 1
#  A[2] = 2
#  A[3] = -2
#  A[4] = 5
#  A[5] = 6
#contains the following example triplets:

#(0, 1, 2), product is −3 * 1 * 2 = −6
#(1, 2, 4), product is 1 * 2 * 5 = 10
#(2, 4, 5), product is 2 * 5 * 6 = 60
#Your goal is to find the maximal product of any triplet.
#the function should return 60, as the product of triplet (2, 4, 5) is maximal.

def solution(A):
    ANS=A[0]*A[1]*A[2]
    for i in range(0,len(A)-2):
        for j in range(1,len(A)-1):
            for k in range(2,len(A)):
                if j>=k or i>=j:
                    continue
                else:
                    if ANS<A[i]*A[j]*A[k]:
                        ANS=A[i]*A[j]*A[k]
    return(ANS)    