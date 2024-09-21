from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    prefix = ""
    max_len = min(map(len, strs))
    for i in range(max_len):
        compare_prefix = zip(strs[:-1], strs[1:])
        has_prefix= all(w1[:i+1] == w2[:i+1] for w1, w2 in compare_prefix)
        if has_prefix:
            prefix += strs[0][i]
    return prefix

def longestCommonPrefix2(strs):
    prefix = ""
    max_len = min(map(len, strs))
    compare_prefix = list(zip(strs[:-1], strs[1:]))
    idx_prefix = 0
    for i in range(max_len):
        has_prefix= all(
            w1[:i+1] == w2[:i+1] for w1, w2 in compare_prefix
        )
        if not has_prefix:
            return prefix + strs[0][:idx_prefix]
        
        idx_prefix += 1
    

    return prefix + strs[0][:max_len]

strs = ["aab", "aaab"]
target = "fl"
res = longestCommonPrefix2(strs)
print("hallooo")
print(res)