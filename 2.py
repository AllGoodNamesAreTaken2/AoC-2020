file = open('2_value')
lines = file.readlines()
all_values = []

for line in lines:
    value = line.replace('\n', '')
    value = value.split(' ')
    all_values.append(value)

valid_numbers = 0

for value in all_values:
    minimun, maximum = value[0].split('-')
    check = value[1].replace(':', '')
    text = value[2]
    counter = 0
    for letter in text:
        if letter == check:
            counter += 1
    if counter <= int(maximum) and counter >= int(minimun):
        valid_numbers += 1



valid_numbers = 0

for value in all_values:
    minimun, maximum = value[0].split('-')
    check = value[1].replace(':', '')
    text = value[2]

    print('TEST')
    first = text[int(minimun) - 1] == check
    second = text[int(maximum) - 1] == check
    if first:
        if not second:
            valid_numbers += 1
    elif second:
        valid_numbers += 1


print(valid_numbers)

