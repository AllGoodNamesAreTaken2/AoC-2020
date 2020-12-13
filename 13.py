from Utils import Base, read_values
import math

file = open('13_value')
first = True

start_time = None
times = []

for line in file.readlines():
    line.strip()
    if first:
        first = False
        start_time = int(line)
    else:
        times = line.split(',')


clean_times = []

for time in times:
    if time == 'x':
        continue
    clean_times.append(int(time))


lowest = start_time * 2
bus_id = None
time_wait = 0

for time in clean_times:
    print('----------')
    print('..........')
    print(start_time)
    print(time)
    test = -(start_time % time) + time + start_time
    if test < lowest:
        lowest = test
        bus_id = time
        time_wait = lowest - start_time
    print(test)


print(time_wait * bus_id)

print('-------------')
print('=============')
print(times)

new_times = []
big = (0, 0)
ind = -1
for time in times:
    ind += 1
    try:
        time = int(time)
        new_times.append(time)
        if time > big[0]:
            big = (time, ind)
    except ValueError:
        new_times.append(time)

run = True
go_time = start_time
print('****************')
match = False

while go_time % big[0] != 0:
    go_time += 1

go_time -= big[1]
big = big[0]

print(go_time)
print('===========')

run = False

while run:
    fail = False
    for i in range(0, len(new_times)):
        time = new_times[i]
        if time == 'x':
            continue
        if (go_time + i) % time != 0:
            fail = True
            break

    go_time += big
    run = fail

go_time -= big
print('GOAL')
print(go_time)

# Above were to slow to count
# Trying new method

synced_values = []
sync_jump = 0
sync_start_time = 0
primes_used = []
twos = 0

print('NEW VERSION!!!')


def get_primes(n):
    print('GET PRIMES FROM: ' + str(n))
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes


def handle_primes(primes, value):
    return_value = []
    if primes[-1] == value:
        return [value]

    for prime in primes:

        if prime == 2:
            while value/prime == int(value / prime) * 1.0:
                value = value / 2
                return_value.append(2)
        if value/prime == int(value / prime) * 1.0:
            return_value.append(prime)

    return return_value


def sync_value(value, offset):
    global synced_values
    global sync_jump
    global sync_start_time
    global twos

    #if len(synced_values) == 0:
    #    synced_values.append((value, offset))
    #    sync_start_time = value
    #    sync_jump = value

    #if sync_start_time == 0:
    #    sync_start_time = start_time


    start = sync_start_time
    times = 1
    left = int(sync_start_time / value) - 2
    times = left
    A = ((times * value) + offset)
    if A < value:
        A = value
    B = sync_start_time

    print('------')
    print(value)
    print(A)
    print(B)
    print(sync_jump)
    print(sync_start_time)
    print('------')

    t_offset = offset

    n = 0
    if offset >= value:
        t_offset = t_offset % value

    while (n * sync_jump + sync_start_time) % value != t_offset:
        n += 1

    print(sync_start_time)
    sync_start_time = (n * sync_jump + sync_start_time)

    print('.....')
    print(sync_start_time)
    print(value)
    print(offset)
    print(sync_jump)
    print('.....')
    primes = get_primes(value)
    primes = handle_primes(primes, value)
    t_twos = 0
    t_used = primes_used.copy()
    for prime in primes:
        if prime == 2:
            t_twos += 1
            continue
        elif prime in t_used:
            t_used.remove(prime)
            continue
        else:
            primes_used.append(prime)

    twos = max(twos, t_twos)

    jump = 1
    t_primes_used = primes_used.copy()
    for two in range(twos):
        t_primes_used.append(2)
    for prime in t_primes_used:
        jump *= prime
    print('Setting jump!')
    sync_jump = jump
    synced_values.append((value, offset))


def test(test_time):
    for test_value, test_offset in synced_values:
        if (test_time + test_offset) % test_value != 0:
            return False

    return True

print('TEST')

#sync_value(4, 0)
#sync_value(5, 1)
#sync_value(6, 2)
#sync_value(2, 0)
#sync_value(4, 0)
#sync_value(8, 0)
#sync_value(14, 0)

print('TEST')
print(primes_used)
print(twos)
print(sync_start_time)
print(sync_jump)
#print(test(42))

sort = {}

sync_jump = int(times[0])
sync_value(sync_jump, 0)
sync_start_time = 0

for i in range(1, len(new_times)):
    value = new_times[i]
    if value == 'x':
        continue
    value = int(value)
    key = value + i * 3
    if key in sort.keys():
        print(key)
        print(sort)
        print(value)
        print(i)
        print('ERROR')
        exit()

    sort[key] = (value, i)

for key in sorted(sort.keys()):
    value, offset = sort[key]
    sync_value(value, offset)


for i in range(len(new_times)):
    break
    test = new_times[i]
    if test == 'x':
        continue
    sync_value(test, i)

    print('**************')
    print('**************')
    print('**************')
    print(synced_values)
    print(sync_jump)
    print(sync_start_time)
    print('**************')
    print('**************')
    print('**************')

print(primes_used)
print(sync_jump)
print(sync_jump - sync_start_time)
print(sync_start_time)
print('FINAL!!')

print(sync_jump - sync_start_time)