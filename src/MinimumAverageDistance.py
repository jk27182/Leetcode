from typing import List
import time
import logging



def timer(func):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        res = func(*args, **kwargs)
        print(f"Function aufruf von {func.__name__} hat {time.perf_counter() - tic}s gedauert.")
        return res
    return wrapper
        

@timer
def minimumAverageDifference_twoPointer(nums: List[int]) -> int:
        min_avg_dist = 10**5 + 1 
        half_nums = len(nums)//2 + 1
        left = 0
        right = len(nums) - 1
        min_idx = 0
        for idx, num in enumerate(nums[:half_nums]):
            left_slice_idx = idx + 1
            right_slice_idx = len(nums) - idx
            
            left_mean_left = sum(nums[:left_slice_idx]) // len(nums[:left_slice_idx])
            if len(nums[left_slice_idx:]) == 0:
                left_mean_right = 0
            else:
                left_mean_right = sum(nums[left_slice_idx:]) // len(nums[left_slice_idx:])
            
            right_mean_left = sum(nums[:right_slice_idx]) // len(nums[:right_slice_idx])
            if len(nums[right_slice_idx:]) == 0:
                right_mean_right = 0
            else:
                right_mean_right = sum(nums[right_slice_idx:]) // len(nums[right_slice_idx:])
            
            left_avg_dist = abs(left_mean_left - left_mean_right)
            right_avg_dist = abs(right_mean_left - right_mean_right)    

            comp_idx, compare_dist = min((idx, left_avg_dist), (len(nums) - idx -1,right_avg_dist), key = lambda x: x[1])
            
            if compare_dist <= min_avg_dist:
                min_avg_dist = compare_dist
                min_idx = comp_idx
        
        return min_idx 

@timer
def minimumAverageDifference(nums: List[int]) -> int:
        min_avg_dist = 10**5 + 1
        min_idx = 0
        for idx, num in enumerate(nums):
            left_slice_idx = idx + 1
            
            left_mean_left = sum(nums[:left_slice_idx]) // len(nums[:left_slice_idx])
            if len(nums[left_slice_idx:]) == 0:
                left_mean_right = 0
            else:
                left_mean_right = sum(nums[left_slice_idx:]) // len(nums[left_slice_idx:])
            
            
            left_avg_dist = abs(left_mean_left - left_mean_right)
            
            if left_avg_dist < min_avg_dist:
                min_avg_dist = left_avg_dist
                min_idx = idx
        
        return min_idx 

inp = [i**2 for i in range(100000)]
res = minimumAverageDifference(inp)
res2 = minimumAverageDifference_twoPointer(inp)
print(res == res2)