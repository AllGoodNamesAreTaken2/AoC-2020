from Utils import Base, read_values

values = read_values('12_value')
print(values)


pos_x = 0
pos_y = 0

way_x = 10
way_y = 1

current_direction = 'E'

dic_dir = {
    'N': 0,
    'E': 90,
    'W': 270,
    'S': 180,
}


dic_dir_rev = {
    0: 'N',
    90: 'E',
    270: 'W',
    180: 'S',
}


def go_direction(dir, val):
    global pos_x
    global pos_y

    print('Current direction = ' + current_direction)
    print('Value = ' + str(val))
    print('Pos = ' + str((pos_x, pos_y)))
    print('=========')

    if dir == 'E':
        pos_x += val
    elif dir == 'W':
        pos_x -= val
    elif dir == 'N':
        pos_y += val
    elif dir == 'S':
        pos_y -= val


def handle_line(line):
    global current_direction
    if 'F' in line:
        go_direction(current_direction, int(line.split('F')[1]))
    elif 'N' in line:
        go_direction('N', int(line.split('N')[1]))
    elif 'E' in line:
        go_direction('E',int(line.split('E')[1]))
    elif 'S' in line:
        go_direction('S',int(line.split('S')[1]))
    elif 'W' in line:
        go_direction('W',int(line.split('W')[1]))
    elif 'L' in line:
        val = dic_dir[current_direction]
        val -= int(line.split('L')[1])
        val = val % 360
        current_direction = dic_dir_rev[val]
    elif 'R' in line:
        print('-------------')
        print('Dir Before=' + current_direction)
        val = dic_dir[current_direction]
        val += int(line.split('R')[1])
        val = val % 360
        current_direction = dic_dir_rev[val]
        print('Dir After=' + current_direction)
        print('-------------')

pos_x = abs(pos_x)
pos_y = abs(pos_y)

print((pos_x, pos_y))
print(pos_x + pos_y)


pos_x = 0
pos_y = 0

#  Part 2


def move_ship(val):
    global pos_x
    global pos_y

    pos_x += way_x * val
    pos_y += way_y * val


def rotate(val):
    global way_x
    global way_y

    while val != 0:
        if val < 0:
            d = -1
            val += 90
        else:
            d = 1
            val -= 90

        new_x = way_y * d
        new_y = way_x * -d
        way_y = new_y
        way_x = new_x


def handle_line2(line):
    global way_y
    global way_x
    if 'F' in line:
        move_ship(int(line.split('F')[1]))
    elif 'N' in line:
        way_y += int(line.split('N')[1])
    elif 'E' in line:
        way_x += int(line.split('E')[1])
    elif 'S' in line:
        way_y -= int(line.split('S')[1])
    elif 'W' in line:
        way_x -= int(line.split('W')[1])
    elif 'L' in line:
        rotate(-int(line.split('L')[1]))
    elif 'R' in line:
        rotate(int(line.split('R')[1]))


for value in values:
    print('-----')
    print((pos_x, pos_y))
    print((way_x, way_y))
    print('-----')
    handle_line2(value)


print((pos_x, pos_y))

pos_x = abs(pos_x)
pos_y = abs(pos_y)
print(pos_x + pos_y)
