def romanLetters(s):
    mapping = {
        "I" : "1",
        "V" : "5",
        "X" : "10",
        "L" : "50",
        "C" : "100",
        "D" : "500",
        "M" : "1000",
    }
    # Letzten Wert merken und dann den Wert danach anshcauen
    occur = {
        "V" : 4,
        "X" : 9,
        "L" : 40,
        "C" : 90,
        "D" : 400,
        "M" : 900,
    }
    minus_map = {
        "I" : 1,
        "X" : 10,
        "C" : 100,
    }
    res = 0
    stack = []
    for idx, num in enumerate(s):
        if minus_map.get(num, False):
            print("in minus map")
            stack.append(minus_map[num])
            continue
        
        if len(stack):
            minus = stack.pop()  
        else:
            minus = 0
        print("mapping", mapping[num])
        translate = mapping[num] - minus
        print(translate)
        res += translate
    return res

roman = "III"
print(romanLetters(roman))