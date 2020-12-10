from Utils import Base, read_values
import itertools
import math

values = read_values('10_value', only_ints=True)
values.sort()

print(values)

biggest = max(values)
print(biggest)


c_1 = 0
c_2 = 0
c_3 = 0

start = 0
index = 0

while start <= biggest:
    try:
        if (start + 1) in values:
            c_1 += 1
            start = values[index]
            index += 1
        elif (start + 2) in values:
            c_2 += 1
            start = values[index]
            index += 1
        elif (start + 3) in values:
            c_3 += 1
            start = values[index]
            index += 1
        elif start == biggest:
            c_3 += 1
            start = values[index]

    except IndexError:
        break

print(c_1)
print(c_2)
print(c_3)

p_1 = c_1
p_2 = c_2
p_3 = c_3


in_straight = {}
s = values.copy()
s.insert(0, 0)
s.append(biggest + 3)
print(s)

i = 0


while True:
    try:
        t = i + 1
        streak = 0
        while s[t] - s[i] == 1:
            streak += 1
            t += 1
            i += 1

        i += 1
        try:
            print('====')
            print(streak)
            print(s[i])
            print('===')
            in_straight[streak] = in_straight[streak] + 1
        except KeyError:
            in_straight[streak] = 1
    except IndexError:
        break

twos = 2 ** in_straight[2]
total = 0

print(in_straight)

test = False
if test:
    in_straight[1] = 0
    in_straight[2] = 1
    twos = 2
    in_straight[3] = 1
    in_straight[4] = 4

try:
    threes = in_straight[3]
except KeyError:
    threes = 0

try:
    four = in_straight[4]
except KeyError:
    four = 0

if threes and four:
    print('T1')
    print(twos)
    print(threes)
    print(four)
    print('====')
    total = twos * (4 ** threes) * (7 ** four)
    print(total)
elif threes:
    print('T2')
    total += twos * (4 ** threes)
elif four:
    print('T3')
    total += twos * (7 ** four)


print(total)

print(in_straight)
