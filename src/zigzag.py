def zigzag(s: str, numRows:int) -> str:
    if numRows == 1:
        return s

    res = []
    row = 0
    idx = 0
    initial_step = 2*numRows - 2
    for row in range(numRows):
        if row == numRows -1 or row == 0:
            step1 = 2*numRows - 2
            step2 = step1
        else:
            step1 = initial_step - 2*(row)
            step2 = initial_step - step1

        counter = 0
        print(f"{row=}, {step1=}, {step2=}")
        while idx < len(s):
            print(f"append {idx=}")
            res.append(s[idx])
            if counter % 2 == 0:
                idx += step1
            else:
                idx += step2
            counter+=1

        idx = row+1

    return "".join(res)

s = "PAYPALISHIRING"

num_rows = 3
result_expected = "PAHNAPLSIIGYIR"

# s = "PAYPALISHIRING"
# num_rows = 4
# result_expected = "PINALSIGYAHRPI"
# s = "ABCDE"
# num_rows = 5
# result_expected = "ABCDE"

print(len(s))
res = zigzag(s, num_rows)
print(res)
print(res == result_expected)
