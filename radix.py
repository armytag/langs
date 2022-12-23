def find_repeating_digits(numerator, denomenator, base):
    digits = []
    remainders = []
    repeating = False
    while not repeating:
        digit, remainder = divmod(numerator, denomenator)
        if remainder in remainders:
            repeating = True
        digits.append(digit)
        remainders.append(remainder)
        if remainder == 0:
            break
        numerator = remainder * base
    return { 'digits': digits, 'remainders': remainders, 'repeating': repeating }

def stringify_digit(value):
    if value >= 10:
        return chr(55+value)
    return chr(48+value)

if __name__ == "__main__":
    print(find_repeating_digits(1, 20, 60))
    for denomenator in range(1, 26):
        result_5 = find_repeating_digits(1, denomenator, 5)
        result_6 = find_repeating_digits(1, denomenator, 6)
        result_7 = find_repeating_digits(1, denomenator, 7)
        result_12 = find_repeating_digits(1, denomenator, 12)
        result_30 = find_repeating_digits(1, denomenator, 30)
        result_60 = find_repeating_digits(1, denomenator, 60)
        # print(denomenator, result)
        # print('0.' + ''.join(map(stringify_digit, result['digits'][1:])))

        places_5 = len(result_5['digits'])-1
        places_6 = len(result_6['digits'])-1
        places_12 = len(result_12['digits'])-1
        places_30 = len(result_30['digits'])-1
        places_60 = len(result_60['digits'])-1
        places_min = min(places_5, places_6, places_12, places_30, places_60)
        places_max = max(places_5, places_6, places_12, places_30, places_60)

        places_5 -= places_min
        places_6 -= places_min
        places_12 -= places_min
        places_30 -= places_min
        places_60 -= places_min

        number_5 = '0.' + ''.join(map(stringify_digit, result_5['digits'][1:]))
        number_6 = '0.' + ''.join(map(stringify_digit, result_6['digits'][1:]))
        number_12 = '0.' + ''.join(map(stringify_digit, result_12['digits'][1:]))
        number_30 = '0.' + ''.join(map(stringify_digit, result_30['digits'][1:]))
        number_60 = '0.' + ''.join(map(stringify_digit, result_60['digits'][1:]))
        number_format = "{:>2}:" + "{:>3}" * 2 + "{:>16}" * 3
        places_format = "{:>2}: " + "{:>2}" + "{:>4}{:>1}" * 5
        # print(number_format.format(denomenator, places_min, places_max, number_5, number_6, number_7, number_12))
        print(places_format.format(denomenator, places_min, places_5, str(result_5['repeating'])[0], places_6, str(result_6['repeating'])[0], places_12, str(result_12['repeating'])[0], places_30, str(result_30['repeating'])[0], places_60, str(result_60['repeating'])[0]))
        # print(f'{denomenator}:\t{number_5}\t{number_6}\t{number_7}\t{number_12}\t{places_min}')