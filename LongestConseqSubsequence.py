from typing import List


def longestConsecutive(nums: List[int]) -> int:

    sorted_nums = sorted(set(nums))
    print(sorted_nums)
    if len(nums) == 0:
        return 0
    cons_seq_len = 1
    max_subseq = cons_seq_len
    for i, num in enumerate(sorted_nums[:-1]):
        print('max_subseq', max_subseq)
        if num + 1 == sorted_nums[i+1]: # will run out of bounds
            print(num, 'counter ', cons_seq_len)
            cons_seq_len += 1
            if max_subseq < cons_seq_len:
                max_subseq = cons_seq_len
        else:
            cons_seq_len = 1 
    return max_subseq
  
inp = [100,4,200,1,3,2]
# inp = []
# inp = [9,1,4,7,3,-1,0,5,8,-1,6]
inp = [1,2,0,1]

print(longestConsecutive(inp))
