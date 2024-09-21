lower = 1
higher = 100
answer = 20


def guess(guess_trial):
    if guess_trial == answer:
        return 0
    if guess_trial > answer:
        return -1
    else:
        return 1

def guessing(low, high):
    middle = (high + low) // 2
    guess_res = guess(middle)
    if guess_res == 0:
        return middle
    if guess_res == 1:
        return guessing(middle+1,high)
    else:
        return guessing(low, middle - 1)

res = guessing(lower, higher)
print(res)