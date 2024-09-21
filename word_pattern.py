def wordPattern(pattern: str, s: str) -> bool:
    sequence_words = s.split(" ")
    pattern_to_word = {}
    word_to_pattern = {}
    
    for (pattern, word) in zip(pattern, sequence_words):
        case1 = word in word_to_pattern and (not pattern in pattern_to_word)
        case2 = pattern in pattern_to_word and (not word in word_to_pattern)
        bijection_match = (pattern_to_word.get(pattern, "") == word) and (word_to_pattern.get(word, "") == pattern)
        # if word in word_to_pattern and (not pattern in pattern_to_word):
        #     return False
        if case1 or case2:
            return False
        else:
            pattern_to_word[pattern] = word
            word_to_pattern[word] = pattern
        
        if not bijection_match:
            return False

    return True

pattern = "aba"
s = "dog cat cat"
# {
#     a : dog,
#     b: cat
# }
# pattern = "abca"
# s = " ".join(["dog", "cat", "cat", "dog"])
# cases for mismatch

# word in words but pattern not in pattern
# pattern in pattern but word not in words
# both in pattern and words but not matching

# abca, [dog, cat, cat, dog]
# {
#     a: dog,
#     b: cat, 
# }
print(wordPattern(pattern, s))