import math
def piles_bananas(piles, h):
    def check(k):
        res = sum(map(lambda pile: math.ceil(pile/ k), piles))
        return res <= h

    # list_of_k = [i for i in range(1, max(piles)+1))]
    left = 1
    right = max(piles) + 1

    while left < right:
        middle = left + (right - left)//2
        print('left', left)
        print('middle', middle)
        print('right', right)
        print('check', check(middle))
        if check(middle):
            right = middle
        else:
            left = middle + 1
        print('---------------')

    return left

piles = [3,6,7,11]
h = 8

print(piles_bananas(piles, h))
