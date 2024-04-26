#!/usr/bin/python3
<<<<<<< HEAD
def to_subtract(list_num):
    to_sub = 0
    max_list = max(list_num)

    for n in list_num:
        if max_list > n:
            to_sub += n

    return (max_list - to_sub)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list_keys = list(rom_n.keys())

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        for r_num in list_keys:
            if r_num == ch:
                if rom_n.get(ch) <= last_rom:
                    num += to_subtract(list_num)
                    list_num = [rom_n.get(ch)]
                else:
                    list_num.append(rom_n.get(ch))

                last_rom = rom_n.get(ch)

    num += to_subtract(list_num)

=======


def roman_to_int(roman_string):
    """Converts a roman numeral to an integer."""
    if (not isinstance(roman_string, str) or
            roman_string is None):
        return (0)

    roman_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    num = 0

    for i in range(len(roman_string)):
        if roman_dict.get(roman_string[i], 0) == 0:
            return (0)

        if (i != (len(roman_string) - 1) and
                roman_dict[roman_string[i]] < roman_dict[roman_string[i + 1]]):
            num += roman_dict[roman_string[i]] * -1

        else:
            num += roman_dict[roman_string[i]]
>>>>>>> 69f966ee05059221ac9911ea4871ad8b5f77a395
    return (num)
