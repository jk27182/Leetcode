def max_avg(nums: list, k:int) -> float:
    left_window = 0
    right_window = k
    best_mean = -float('inf')

    while right_window < len(nums):
        mean_trial = sum(nums[left_window:right_window]) / k
        best_mean = max(best_mean, mean_trial)
        left_window+=1
        right_window+=1

    return best_mean
