def lengthOfLongestSubstring(s: str) -> int:
    # sliding window
    # start on same character, and keep track of already seen characters
    # can whitespaces be in the string?
    # if everything is fine, make window bigger by moving right pointer and update current max length
    # see duplicate: whenever I see a duplicate value, set the left pointer one to the right of the first occurence of this element -> keep track with hasmap of index
    # and update index of hash map

    char_index = {}
    left = 0
    max_counter = 0

    for right, char in enumerate(s):
        if char in char_index:
            # two cases possible, repeat inside current window, or outsideafter
            if char_index[char] < left:
                char_index[char] = right
            else:
                left = char_index[char] + 1
                char_index[char] = right
        else:
            char_index[char] = right

        max_counter = max(max_counter, (right - left) + 1)

    return max_counter


s = 'abcadaabb'
s = "tmmzuxt"
s = "aabaab!bb"

# s = 'advdef'

# left: 0  1 4k 6    
# right  0  1   2, 3, 4 5 6
# char_index: a:6, b:1 c:2, d:4
# max_counter: 1, 2, 3, 3, 4, 2, 1, 

print(lengthOfLongestSubstring(s))