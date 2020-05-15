def isSubTree(T1, T2):
    if T1 is None and T2 is None:
        return True
    if T1 is None or T2 is None:
        return False
    if (T1.data == T2.data) and isSubTree(T1.right,T2.right) and isSubTree(T1.left,T2.left):
        return True
    return isSubTree(T1.left,T2) or isSubTree(T1.right,T2)