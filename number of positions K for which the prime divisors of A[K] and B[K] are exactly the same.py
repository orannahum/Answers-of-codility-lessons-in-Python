"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A, B is an integer within the range [1..2,147,483,647]."""
    
A=[15,10,3,10,24]
B=[75,30,5,1000,72]
#A
afterdivideA=A
which_primes_for_A = [[[] for i in range(len(A))] for j in range(1)]
for i in range(0,len(A)):
    primesA=[]
    lower = 1
    upper = A[i]
    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for J in range(2, num):
               if (num % J) == 0:
                   break
           else:
               primesA.append(num)
    for k in range(0,len(primesA)):
               if   A[i]%primesA[k]==0:
                   while afterdivideA[i]%primesA[k]==0:
                       afterdivideA[i]=afterdivideA[i]//primesA[k]
                   which_primes_for_A[0][i].append(primesA[k])
#B                   
afterdivideB=B
which_primes_for_B = [[[] for i in range(len(B))] for j in range(1)]
for i in range(0,len(B)):
    primesB=[]
    lower = 1
    upper = B[i]
    for num in range(lower, upper + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for J in range(2, num):
               if (num % J) == 0:
                   break
           else:
               primesB.append(num)
    for k in range(0,len(primesB)):
               if   B[i]%primesB[k]==0:
                   while afterdivideA[i]%primesB[k]==0:
                       afterdivideB[i]=afterdivideA[i]//primesB[k]
                   which_primes_for_B[0][i].append(primesB[k])       
                   
match_primes=0
for j in range(0,len(A)):  
     if which_primes_for_B[0][j]==which_primes_for_A[0][j]:
         match_primes=match_primes+1
         
print(match_primes)                   
                      
                       
                            
                   
               
               