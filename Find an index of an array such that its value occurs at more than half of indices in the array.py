#An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
#For example, consider array A such that

# A[0] = 3    A[1] = 4    A[2] =  3
# A[3] = 2    A[4] = 3    A[5] = -1
# A[6] = 3    A[7] = 3
#The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
def solution(A):
    list_of_number=[]
    numbers_time=[0]*len(A)
    if len(A)==0:
        return(-1)
          
    if len(A)==1:
        return(A[0])
         
    for i in range(0,len(A)):
        if A[i] in list_of_number:
          index_of_number=list_of_number.index(A[i])  
          numbers_time[index_of_number]=  numbers_time[index_of_number]+1
        if A[i] not in list_of_number: 
           list_of_number.append(A[i])
        
    number_of_most_value_in_array=max(numbers_time)+1
    most_value_in_array=list_of_number[numbers_time.index(max(numbers_time))]      

    if len(A)%2 == 0 :
        more_then_half= len(A)/2+1
        if number_of_most_value_in_array>=more_then_half:
            return(A.index(most_value_in_array))        
        else:
            return(-1)
    else :
        more_then_half= len(A)//2+1
        if number_of_most_value_in_array>=more_then_half:
            return(A.index(most_value_in_array))
        else:
            return(-1)
        
A=[]
print(solution(A))       