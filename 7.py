from Utils import Base, read_values

values = read_values('7_value')


class Test(Base):
    def __init__(self):
        self.d_bags = []
        self.bags = {}
        self.r_bags = {}
        self.valid_bags = []

    def check_value(self, value):
        parts = value.split('bag')
        first = True
        other_bags = []
        o_r_bags = []
        new_bag = None
        for part in parts:
            if first:
                new_bag = parts[0].split(' ')
                new_bag = new_bag[0] + ' ' + new_bag[1]
                first = False
            else:
                if '.' in part or 'no other' in part:
                    continue
                other = part.split(' ')
                if other[1] == 'contain':
                    number = int(other[2])
                else:
                    number = int(other[1])
                other = other[-3] + ' ' + other[-2]
                val = (other, number)
                o_r_bags.append(val)
                other_bags.append(other)

        if new_bag is not None and other_bags != []:
            if 'shiny gold' in other_bags:
                self.d_bags.append(new_bag)
                self.r_bags[new_bag] = o_r_bags
            else:
                self.bags[new_bag] = other_bags
                self.r_bags[new_bag] = o_r_bags

    def link_bags(self):
        for bag in self.d_bags:
            if bag not in self.valid_bags:
                self.valid_bags.append(bag)
        for key, other in self.bags.items():
            for bag in other:
                if key not in self.valid_bags:
                    if self.test_bag(bag):
                        self.valid_bags.append(key)

    def test_bag(self, bag):
        if bag in self.d_bags or bag in self.valid_bags:
            return True
        try:
            tests = self.bags[bag]
            for test in tests:
                test = self.test_bag(test)
                if test:
                    return True
            return False
        except KeyError:
            return False

    def new_count_bags(self):
        result = self.new_count_bag('shiny gold', 0)
        print('NEW!')
        print(result)

    def new_count_bag(self, m_bag, tb):
        try:
            bags = self.r_bags[m_bag]
        except KeyError:
            return 1
        result = 1  # Had this on 0 which were giving me troubles...

        print('bag=' + str(m_bag) + ', tb=' + str(tb) + ', bags=' + str(bags))

        for bag, times in bags:
            #result += times

            t = self.new_count_bag(bag, times)
            print('Bag=' + bag)
            print(t)
            result += t * times
            print(result)

        #result += tb

        if m_bag == 'shiny gold2':
            print('YES')
            for bag, times in bags:
                result += times
        return result


    def count_bags(self):
        bags = self.r_bags['shiny gold']
        print(bags)
        result = 0
        for bag, times in bags:
            result += times
            c_value = self.count_bag(bag, times) * times
            print(bag)
            print(times)
            print(c_value)
            result += c_value
        return result

    def count_bag(self, bag, times):
        try:
            bags = self.r_bags[bag]
            #print(bags)
            result = 0
            for bag, times in bags:
                c_value = self.count_bag(bag, times) * times
                print(bag)
                print(times)
                print(c_value)
                result += c_value
            #print(result)
            return result
        except KeyError:
            return times

def make_class_vars(item, attrs):
    item.make_attributes(attrs)


test = Test()

for value in values:
    test.check_value(value)

t_value = 0
test.link_bags()

while t_value != len(test.valid_bags):
    t_value = len(test.valid_bags)
    test.link_bags()
    print(t_value)

print(test.valid_bags)

#print(test)
#test.new_count_bags()

