
file = open('8_value')
lines = file.readlines()


jmp_to_change = 0


def do():
    try:
        values = {}
        key = 0
        current_jmp = 0

        for line in lines:
            action, action_value = line.split(' ')
            action_value = int(action_value)
            if action == 'jmp':
                if current_jmp == jmp_to_change:
                    action = 'nop'
                current_jmp += 1
            values[key] = {
                'visited': False,
                'action': action,
                'action_value': action_value,
                'oder': None
            }
            key += 1


        key = 0
        order = 0
        acc = 0

        def visit():
            if not values[key]['visited']:
                values[key]['visited'] = True
                values[key]['order'] = order
                return False
            return True

        run = True
        while run:
            test = False
            action = values[key]['action']
            value = values[key]['action_value']
            if action == 'nop':
                test = visit()
                key += 1
            elif action == 'acc':
                test = visit()
                if not test:
                    acc += value
                    key += 1
            elif action == 'jmp':
                test = visit()
                key += value

            if test:
                run = False
            order += 1
    except KeyError:
        print('KeyError')
        print(acc)


while True:
    do()
    jmp_to_change += 1
