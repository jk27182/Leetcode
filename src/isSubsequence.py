from typing import List

def isSubsequence(s, t) -> int:
    if len(s) > len(t):
        return False
    
    if len(s) == len(t):
        return s == t
    
    if s == "":
        return True
    
    else:
        idx = 0
        for c1 in s:
            try:
                idx = t.index(c1, idx) + 1
                print(idx)
                print(c1)
                print(t[idx:])
            except ValueError as e:
                print(e)
                print(c1)
                return False

        return True 


s = "twn"
t = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"

a = [2, -1, -1]
a = [1, 7, 1, 9]
res = isSubsequence(s, t)
print(res)