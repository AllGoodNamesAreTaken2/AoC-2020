from Utils import Base, read_values

values = read_values('11_value')

print(values)

dic = {}

for i in range(len(values)):
    for j in range(len(values[0])):
        dic[(i, j)] = values[i][j]

run = True

max_row = len(values)
max_col = len(values[0])


def get_values(currents, row, col):
    vals = []

    for i in range(-1, 2):
        for j in range(-1, 2):
            dir_i = i
            dir_j = j
            try:
                if i == 0 and j == 0:
                    continue
                while currents[(row + i, col + j)] == '.':
                    i += dir_i
                    j += dir_j

                vals.append(currents[(row + i, col + j)])
                i = dir_i
            except KeyError:
                i = dir_i

    return vals


def check_near(value, currents, row, col):
    if value == '.':
        return
    elif value == 'L':
        vals = get_values(currents, row, col)
        if not '#' in vals:
            dic[(row, col)] = '#'
    elif value == '#':
        vals = get_values(currents, row, col)
        if row == 10 and col == 10:
            print(vals)
        count = 0
        while '#' in vals:
            count += 1
            vals.remove('#')
        if count > 4:
            dic[(row, col)] = 'L'


test = 0


def print_dic(vals:dict):
    text = ''
    for i in range(len(values)):
        text += '\n'
        for j in range(len(values[0])):
            text += vals[(i, j)]

    print(text)

print_dic(dic)

while run:
    #test += 1
    #if test == 8:
    #    exit()
    current_state = dic.copy()
    for i in range(len(values)):
        for j in range(len(values[0])):
            check_near(current_state[(i, j)], current_state, i, j)

    if current_state == dic:
        run = False

    #print_dic(dic)

seats = 0

for item in dic.values():
    if item == '#':
        seats += 1

print(seats)
