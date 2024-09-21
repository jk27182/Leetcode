from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # sort values of entry and hash them as a key in a dictionary
    # append the corresponding array value to the value list
    from collections import defaultdict
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)


    return list(anagrams.values())
    # set_list = []
    # for word in strs:
    #     set_list.append(set(word))

strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams(strs))