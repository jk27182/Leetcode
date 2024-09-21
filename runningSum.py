from typing import List

def runningSum(nums: List[int]) -> List[int]:
    res = [num for num in nums]
    for i, num in enumerate(res[1:]): 
        print("testen", i, res)
        res[i] = res[i] + res[i-1]
        
    return res
    
a = [1,2,3,4]
test = [1,3,7,11]

print(a)
print(test)
print(runningSum(a))
