def push_in_stack(x):
    global queue_1
    global queue_2
    queue_1.append(x)
    
    
def pop_from_stack():

    global queue_1
    global queue_2
    ans = -1
    if len(queue_1) == 0:
        return ans  
    else:
        ans =  queue_1.pop()
        return ans
