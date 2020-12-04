file = open('4_value')
lines = file.readlines()
all_values = []


class Passport:
    def __init__(self):
        self.byr = None
        self.iyr = None
        self.eyr = None
        self.hgt = None
        self.hcl = None
        self.ecl = None
        self.pid = None
        self.cid = None

    def is_present(self):
        attrs = vars(self)
        for key, value in attrs.items():
            if key == 'cid':
                continue
            elif value is None:
                return 0
        return 1

    def is_valid(self):
        attrs = vars(self)
        for key, value in attrs.items():
            if key == 'cid':
                continue
            elif key == 'byr':
                byr = int(value)
                if not (byr >= 1920 and byr <= 2002):
                    print('byr')
                    return 0
            elif key == 'iyr':
                byr = int(value)
                print(byr)
                if not (byr >= 2010 and byr <= 2020):
                    print('iyr')
                    return 0
            elif key == 'eyr':
                byr = int(value)
                if not (byr >= 2020 and byr <= 2030):
                    print('eyr')
                    return 0
            elif key == 'hgt':
                if 'cm' in value:
                    value = value.replace('cm', '')
                    byr = int(value)
                    if not (byr >= 150 and byr <= 193):
                        print('hgt')
                        return 0
                elif 'in' in value:
                    value = value.replace('in', '')
                    byr = int(value)
                    if not (byr >= 59 and byr <= 76):
                        print('hgt')
                        return 0
                else:
                    print('byr')
                    return 0
            elif key == 'hcl':
                valids = '0123456789abcdef'
                if '#' == value[0] and len(value) == 7:
                    for c in value[1:]:
                        if c.lower() not in valids:
                            print('byr')
                            return 0
                else:
                    print('hcl')
                    return 0
            elif key == 'ecl':
                valids = ['amb', 'blu', 'brn', 'gry', 'hzl', 'grn', 'oth']
                test = False
                for valid in valids:
                    if valid == value:
                        test = True
                if not test:
                    print('ecl')
                    return 0
            elif key == 'pid':
                if len(value) != 9:
                    print('pid')
                    return 0
                valids = '0123456789'
                for c in value:
                    if c not in valids:
                        print('pid')
                        return 0
        return 1

    def handle_part(self, part):
        key, value = part.split(':')
        setattr(self, key, value)

    def handle_line(self, parts):
        for part in parts:
            self.handle_part(part)

    def __str__(self):
        attrs = vars(self)
        return ''.join("\n%s: %s" % item for item in attrs.items())


new_passport = Passport()


for line in lines:
    value = line.replace('\n', '').split(' ')
    if value == ['']:
        all_values.append(new_passport)
        new_passport = Passport()
    else:
        new_passport.handle_line(value)

all_values.append(new_passport)
is_present = 0
is_valid = 0

for value in all_values:
    test = value.is_present()
    is_present += test
    if test:
        test = value.is_valid()
        is_valid += test
        if test:
            print(value)


print(is_present)
print(is_valid)
