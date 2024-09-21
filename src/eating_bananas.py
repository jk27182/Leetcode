def minEatingSpeed(piles, h) -> int:
    import math

    def is_valid(speed):
        hours = 0
        for elem in piles:
            hours += math.ceil(elem / speed)
        return hours <= h
    
    left = 1
    right = max(piles)

    while left < right:
        middle = left + (right - left) // 2
        if is_valid(middle):
            right = middle
        else:
            left = middle + 1
    
    return left
                



piles = [30,11,23,4,20]
h = 5
print(minEatingSpeed(piles, h))