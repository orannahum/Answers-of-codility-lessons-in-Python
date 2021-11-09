"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:
    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:
0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.
Write a function:
that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""
def solution(A):
    count=0
    for i in range(0,len(A)-1):
            most_common1 = max(A[0:i+1], key = A.count)
            if A[0:i+1].count(most_common1)<=(i+1)/2:
                most_common1=max(A)+1
            most_common2 = max(A[i:len(A)], key = A.count)
            if A[i+1:len(A)].count(most_common2)<=(len(A)-(i+1))/2:
                most_common1=max(A)+2
                
                
            if most_common1==most_common2:
                count = count +1
    return(count)            


