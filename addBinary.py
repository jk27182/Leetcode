def addBinary(a: str, b: str) -> str:
    binary_add_table = {
        (0,0): (0,0),
        (1,0): (1,0),
        (0,1): (1,0),
        (1,1): (0,1),
    }
    longer_string = max(a,b)
    shorter_string = min(a, b)
    shorter_string = '0'*(len(longer_string) - len(shorter_string)) + shorter_string
    print('longer string', longer_string)
    print('shorter string', shorter_string)
    res_string = ''
    ergebnis, rest = binary_add_table[
        int(longer_string[-1]), int(shorter_string[-1])
    ]
    res_string = str(ergebnis) + res_string 
    print('erster res string', res_string)
    reversed_a_wo_last = longer_string[:-1][::-1]
    reversed_b_wo_last = shorter_string[:-1][::-1]
    print('reversed a', reversed_a_wo_last)
    print('reversed b', reversed_a_wo_last)
    for bit_a, bit_b in zip(
        reversed_a_wo_last,
        reversed_b_wo_last
    ):
        print('bit a',bit_a)
        print('bit b',bit_b)
        ergebnis, rest_neu = binary_add_table[
            int(bit_a), int(bit_b)
        ]
        ergebnis, uber_rest = ergebnis ^ rest
        res_string = str(ergebnis) + res_string 

        print('rest bevor', rest, 'rest neu', rest_neu)
        rest = rest_neu
        print('rest danach', rest)

        print('ergbnis_trial', res_string )
    if rest == 1:
        res_string = str(rest) + res_string

    return res_string

a = '11'
b = '1'

print(addBinary(a,b))