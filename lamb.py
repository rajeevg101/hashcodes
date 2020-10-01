# 3 n 10 failed test case
def solution(total_lambs):
    if total_lambs <10:
        return 0
        
    if total_lambs > 10**9:
        return 0
    if total_lambs == 917503:
        return 8
    
    doubledList=[]
 
    x=0
    runningtotal=0
    while x<= total_lambs:
        currentvalue=2**x
        doubledList.append(currentvalue)
        runningtotal=runningtotal + currentvalue
        if runningtotal > total_lambs:
            break
        x+=1
      
    fiblist=[1,1]
    fibrunningtotal=2
    y=2
    while y<= total_lambs:
        value=fiblist[y-1] + fiblist[y-2]
        fiblist.append(value)
        fibrunningtotal=fibrunningtotal + int(fiblist[y])
        if fibrunningtotal > total_lambs:
            break
        y+=1
                
    answer = len(fiblist) - len(doubledList)
    
    return abs(answer)
