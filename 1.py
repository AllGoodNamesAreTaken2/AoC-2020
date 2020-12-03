file = open('1_value')
lines = file.readlines()
all_values = []

for line in lines:
    value = int(line.replace('\n', ''))
    all_values.append(value)


for a in all_values:
    for b in all_values:
        for c in all_values:
            if a + b +  c== 2020:
                print(a)
                print(b)
                print(c)
                print(a * b * c)

print(all_values)

