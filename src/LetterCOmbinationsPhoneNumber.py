from typing import List
import itertools

def letterCombinations(digits: str) -> List[str]:
    # itertools.product
    mapping = {
        "":[],
        "2": list("abc"),
        "3": list("def"),
        "4": list("ghi"),
        "5": list("jkl"),
        "6": list("mno"),
        "7": list("pqrs"),
        "8": list("tuv"),
        "9": list("wxyz"),
        
    }
    if digits == "":
        return []
    l = [mapping[digit] for digit in digits]
    product = map("".join, list(itertools.product(*l)))
    return list(product)

case1 = "43"
res = letterCombinations(case1)
print(res)