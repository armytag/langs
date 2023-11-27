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
    print(find_repeating_digits(1, 2, 5))
    bases = [5, 7, 12, 30]
    places_format = "{:>2}: " + "{:>3}" + "{:>4}{:>1}" * len(bases)
    header_args = ['D', 'Min']
    extra_places = []
    extra_min = 0
    reps_places = []
    for base in bases:
        header_args.append(base)
        header_args.append('')
        extra_places.append(0)
        reps_places.append(0)
    print(places_format.format(*header_args))
    for denomenator in range(1, 21):
        if denomenator == 17:
            continue
        result_list = []
        places_list = []
        for i, base in enumerate(bases):
            result = find_repeating_digits(1, denomenator, base)
            result_list.append(result)
            places = len(result['digits'])-1
            places_list.append(places)
            if result['repeating']:
                reps_places[i] += 1
        places_min = min(places_list)
        places_max = max(places_list)
        extra_min += places_min
        places_adjusted = [ x - places_min for x in places_list ]
        for i, adj in enumerate(places_adjusted):
            extra_places[i] += adj
        format_args = [denomenator, places_min]
        for i, base in enumerate(bases):
            format_args.append(places_adjusted[i])
            format_args.append(str(result_list[i]['repeating'])[0])
        print(places_format.format(*format_args))
    extra_args = ['E', extra_min] 
    for extra in extra_places:
        extra_args.append(extra)
        extra_args.append('')
    print(places_format.format(*extra_args))
    reps_args = ['R', ''] 
    for reps in reps_places:
        reps_args.append(reps)
        reps_args.append('')
    print(places_format.format(*reps_args))
