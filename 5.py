from Utils import read_values, Base

values = read_values('5_value')


class Test(Base):
    row = list(range(0, 128))
    column = list(range(0, 8))

    def handle_char(self, c):
        if c == 'F':
            limit = int(len(self.row) / 2)
            self.row = self.row[:limit]
        elif c == 'B':
            limit = int(len(self.row) / 2)
            self.row = self.row[limit:]
        elif c == 'R':
            limit = int(len(self.column) / 2)
            self.column = self.column[limit:]
        elif c == 'L':
            limit = int(len(self.column) / 2)
            self.column = self.column[:limit]

    def count_id(self):
        id_value = self.row[0] * 8 + self.column[0]
        return id_value


highest = 0
ids = []

for value in values:
    test = Test()
    for char in value:
        test.handle_char(char)

    test_value = test.count_id()
    ids.append(test_value)
    if test_value > highest:
        highest = test_value

print(highest)  # Part 1

ids.sort()
for index in range(ids[0], ids[-1] + 1):
    if index not in ids:
        print(index)  # Part 2
