
test = '6,3,15,13,1,0'

numbers = test.split(',')
spokens = {}


class Spoken:
    def __init__(self):
        self.last = None
        self.previous = None

    def get_value(self, turn):
        value = 0
        if self.last is not None and self.previous is not None:
            value = self.last - self.previous

        try:
            spokens[value].spoke(turn)
        except KeyError:
            spoken = Spoken()
            spoken.spoke(turn)
            spokens[value] = spoken
        #print(self)
        #print('TURN ' + str(turn) + ' VALUE ' + str(value))
        return value

    def spoke(self, turn):
        self.previous = self.last
        self.last = turn

    def __str__(self):
        attrs = vars(self)
        return ''.join("\n%s: %s" % item for item in attrs.items())


turn = 0
for number in numbers:
    turn += 1
    spoken = Spoken()
    spokens[int(number)] = spoken
    spoken.spoke(turn)
    #print('0TURN ' + str(turn) + ', VALUE ' + str(number))

value = 0
while turn < 30000000:
    turn += 1
    # Find new number
    try:
        spoken = spokens[value]
        value = spoken.get_value(turn)
        #print('1TURN ' + str(turn) + ', VALUE ' + str(value))
    except KeyError:
        spoken = Spoken()
        spokens[value] = spoken
        value = spoken.get_value(turn)
        #print('2TURN ' + str(turn) + ', VALUE ' + str(value))

print(value)

