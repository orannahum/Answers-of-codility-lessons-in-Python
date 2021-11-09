
#A small frog wants to get to the other side of the road. The frog is currently 
#located at position X and wants to get to a position greater than or equal to Y. 
#The small frog always jumps a fixed distance, D.
#  X = 10
#  Y = 85
#  D = 30
#  output = 4

def solution(X, Y, D):
    if ((Y-X)%D)== 0:
        L=int((Y-X)/D)
    else:
        L=int((Y-X)/D)+1
    return(L)




