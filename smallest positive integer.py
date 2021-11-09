#
#Write a function:
#def solution(A)
#that, given an array A of N integers, returns the smallest positive integer (greater than 0) 
#that does not occur in A.

#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#Given A = [1, 2, 3], the function should return 4.
#Given A = [1, 2, 2], the function should return 3.
#Given A = [−1, −3], the function should return 1.

#Write an efficient algorithm for the following assumptions:
#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    # write your code in Python 3.6
    positive_int=1
    for i in range(1, len(A)+1):

            if positive_int in A and len(A) != positive_int:
                positive_int=positive_int+1
                continue
            if positive_int == len(A):
                positive_int=positive_int+1
                break
            else:
                break
    return(positive_int)    
        