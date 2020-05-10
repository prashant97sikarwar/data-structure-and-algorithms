def _push(a,n):
    st = []
    flag = 1000000000
    for i in range(n):
        st.append(a[i])
        flag = min(flag,a[i])
        st.append(flag)
    return st
def _getMinAtPop(stack):

    while len(stack) > 0:
        print(stack.pop(),end=' ')
        stack.pop()
    return
    
