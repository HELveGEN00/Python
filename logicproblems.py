#rim in arabic
def int_to_roman(num: int):
    # value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    # symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    dict_first = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
    }

    res = ""
    for i in dict_first:
        while num >= i:
            res += dict_first[i]
            num -= i
    return res


print(int_to_roman(1000))

#string
def checkio(s):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[s // 1000]
    h = hunds[s // 100 % 10]
    te = tens[s // 10 % 10]
    o = ones[s % 10]
    return print(f"{t}{h}{te}{o}")


checkio(3123)


integers = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)


def roman_to_arabic(roman):
    result = 0
    for i, c in enumerate(roman):
        if i + 1 < len(roman) and integers[roman[i]] < integers[roman[i + 1]]:
            result -= integers[roman[i]]
        else:
            result += integers[roman[i]]
    print(result)
    return str(result)

roman_to_arabic("DCXV")