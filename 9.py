from Utils import Base, read_values

values = read_values('9_values', only_ints=True)

last_n = []
length = 25
master_n = 0

for value in values:
    if len(last_n) < length:
        last_n.append(value)
    else:
        valid = False
        for n in last_n:
            test = value - n
            if test in last_n:
                valid = True
                break
        if not valid:
            print(value)  # Part 1
            master_n = value
            break

        last_n.pop(0)
        last_n.append(value)

start_index = 0

for value in values:
    test = master_n - value
    test_vs = [value]
    test_index = start_index + 1
    while test > 0:
        try:
            tt = values[test_index]
            test -= tt
            test_index += 1
            test_vs.append(tt)
        except IndexError:
            break

    if test == 0:
        print(str(start_index))
        smallest = min(test_vs)
        biggest = max(test_vs)
        print(smallest + biggest)  # Part 2

        break

    start_index += 1
