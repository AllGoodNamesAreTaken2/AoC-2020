from Utils import Base, read_values

file = open('6_value')
lines = file.readlines()


class GroupsAnswer(Base):

    def count_max(self):
        pass

    def count_people(self):
        return len(self.abc)

    def count_answers(self):
        answers = []
        for person in self.abc:
            for char in person:
                if char not in answers:
                    answers.append(char)

        return len(answers)

    def count_same(self):
        answers = []
        for person in self.abc:
            for char in person:
                valid_char = True
                for other in self.abc:
                    if char not in other:
                        valid_char = False
                        break
                if valid_char:
                    if char not in answers:
                        answers.append(char)

        return len(answers)


def make_class_vars(item, attrs):
    item.make_attributes(attrs)


test = GroupsAnswer()
test.abc = []

values = []

for line in lines:
    line = line.strip()
    if line == '':
        values.append(test)
        test = GroupsAnswer()
        test.abc = []
    else:
        test.abc.append(line)
values.append(test)

score = 0

for value in values:
    #print(value)
    #print(value.count_people())
    #print(value.count_answers())
    score += value.count_same()

print(score)
