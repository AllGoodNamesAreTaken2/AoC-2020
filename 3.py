file = open('3_value')
lines = file.readlines()
all_values = []
for line in lines:
    value = line.replace('\n', '')
    all_values.append(value)


def trees(step, skip=False):
    score = 0
    length = len('.......#................#......')
    #length = len('.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#')
    index = 0

    test = 0
    next_skip = False
    for value in all_values:
        if next_skip:
            next_skip = False
            continue
        if value[index] == '#':
            score += 1
        index += step
        index = index % length
        if skip:
            next_skip = True
    print(score)
    return score


a = trees(1)
b = trees(3)
c = trees(5)
d = trees(7)
e = trees(1, True)

#print(a)
#print(b)
#print(c)
#print(d)
#print(e)

print(a * b * c * d * e)
