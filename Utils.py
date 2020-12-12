

def read_values(file, only_ints=False, split_on=None):
    file = open(file)
    lines = file.readlines()
    values = []

    for line in lines:
        line = line.strip()
        if line == '':
            continue
        if split_on is not None:
            line = line.split(split_on)
        if only_ints:
            if isinstance(line, list):
                holder = []
                for value in line:
                    holder.append(int(value))
                line = holder
            else:
                line = int(line)

        values.append(line)

    return values


class Base:
    def make_attributes(self, attrs):
        for attr in attrs:
            setattr(self, attr, None)

    def __str__(self):
        attrs = vars(self)
        return ''.join("\n%s: %s" % item for item in attrs.items())

    def set_var(self, key, value):
        setattr(self, key, value)


class Test(Base):
    pass


if __name__ == '__main__':
    test = Test()
    test.make_attributes(['we', 'eweq'])
    test.set_var('twe', 23)
    print(test)
