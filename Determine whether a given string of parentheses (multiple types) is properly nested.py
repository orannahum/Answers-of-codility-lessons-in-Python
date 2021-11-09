#A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

#S is empty;
#S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
#S has the form "VW" where V and W are properly nested strings.
#For example, the string "{[()()]}" is properly nested but "([)()]" is not.

#that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#3For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [0..200,000];
#string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".


def solution(S):
    for k in range(0,int(len(S)/2)):
      S= S.replace('()','').replace('[]','').replace('{}','') 
    if S=='':
        ANS=1
    else:
        ANS=0   
    return(ANS)  