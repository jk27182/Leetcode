from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # need to track which characters are at which position -> hash table
        # sliding window ansatz, so lange Window expanden, bis ein character kommt, welcher noch nicht in hast table ist
        # den character erstzen mit bisherigen character um so window weiter zu vergrößern
        # das ganze kann man k mal machen, danach muss man Window weiterschieben

        left = 0
        max_substring = 0
        cur_sub_str = s[0]
        queue = []
        right = 0
        char_counter = defaultdict(int)
        char_counter
        # for right, char in enumerate(s):
        while right < len(s):
            char = s[right]
            if char == cur_sub_str:
                char_counter[char] += 1
                max_substring = max(max_substring, (right - left) + 1)
            #     # continue on
                right+=1
            else:
                if char_counter[cur_sub_str] + k >= (right - left +1):
                    char_counter[char] += 1
                    max_substring = max(max_substring, (right - left) + 1)
                    queue.append(right)
                    right += 1
                else:
                    # k changes are not enough anymore, shift window to that Element, which was first different
                    left = queue.pop(0)
                    cur_sub_str = s[left]

        return max_substring


s = "AABABBA"
k = 1
# Output: 4

s = "ABEFE"
k = 2
# Output: 4
print(Solution().characterReplacement(s, k))


            # else:
            #     # char_positions[char].append(right)
            #     queue.append((char, right))
            #     if counter < k:
            #         counter += 1
            #         max_substring = max(max_substring, (right - left) + 1)
            #         right+=1
            #     else:
            #         # over limit, reset counter an move left to element which was first out of order
            #         counter = 0
            #         # get first element that was different
            #         cur_sub_str, left = queue.pop(0)
            #         right = left
            #         max_substring = max(max_substring, (right - left) + 1)