#A non-empty array A consisting of N integers is given.

#A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

#The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

#For example, array A such that:
#    A[0] = 3
#    A[1] = 2
#    A[2] = 6
#    A[3] = -1
#    A[4] = 4
#    A[5] = 5
#    A[6] = -1
#    A[7] = 2
#contains the following example double slices:
#double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
#double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
#double slice (3, 4, 5), sum is 0.
#The goal is to find the maximal sum of any double slice.
#that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.
#the function should return 17, because no double slice of array A has a sum of greater than 17.

def solution(A):

    max_slice=0
    B=[]
    for x in range(0,len(A)-2):
        for y in range(1,len(A)-1):
            for z in range(2,len(A)):
                if x<y<z:
                    for i in range(x,z+1):
                        B.append(A[i])
                    SUM_B=sum(B)-A[x]-A[z]-A[y]
                    B=[]
                    if max_slice<SUM_B:
                        max_slice=SUM_B
    return(max_slice)              