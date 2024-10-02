from typing import List
def longestCommonPrefix(strs: List[str]) -> str:
    i = 1
    prefix = ""
    if len(strs) == 1:
        return strs[0]

    min_length = min((len(s) for s in strs))

    while i <= min_length:
        prefix_tmp = strs[0][:i]
        print("prefix_tmp", prefix_tmp)
        for s in strs[1:]:
            if not s[:i] == prefix_tmp:
                return prefix
        prefix = prefix_tmp
        print(prefix)
        i+=1


    return prefix

strs = ["ab", "a"]
print(longestCommonPrefix(strs))