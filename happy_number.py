def isHappy(n: int) -> bool:
    happy_sum = sum(int(x)**2 for x in str(n))
    sum_tracker = {happy_sum}
    while happy_sum != 1:
        happy_sum = sum(int(x)**2 for x in str(happy_sum))
        if happy_sum in sum_tracker:
            return False

        sum_tracker.add(happy_sum)

    return True

print(isHappy(123456789123456789)) 