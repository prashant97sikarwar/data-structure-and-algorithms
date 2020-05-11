
def qPush(x,stack1,stack2):
    
    while len(stack1) != 0:
        stack2.append(stack1.pop())
    stack1.append(x)
    while len(stack2) != 0:
        stack1.append(stack2.pop())
    
def qPop(stack1,stack2):
    
  
    if len(stack1) == 0:
        return -1
    return stack1.pop()


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            
            if qtyp_qry[i]==1:
                qPush(qtyp_qry[i+1],stack1,stack2)
                
                i+=2
            else:
                print(qPop(stack1,stack2),end=' ')
                i+=1
                
        print()
