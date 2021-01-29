from Utils import Base, read_values

values = read_values('test')
print(values)


def int_to_bits(int_val):
    bits = "000000000000000000000000000000000000"
    int_val = "{0:b}".format(int_val)
    return bits[:len(bits) - len(int_val)] + int_val


class Mask(Base):
    def add_new_med(self, mem_key, mem_value):
        try:
            mem = self.mems[mem_value]
        except KeyError:
            mem = "000000000000000000000000000000000000"
        if mem_value == 0:
            bits = "000000000000000000000000000000000000"
        else:
            bits = "{0:b}".format(mem_value)
        #full_bits = "000000000000000000000000000000000000"
        #full_bits = full_bits[:len(full_bits) - len(bits)] + bits
        mem = mem[:len(mem) - len(bits)] + bits
        for i in range(len(self.mask)):
            if self.mask[i] != 'X':
                mem = mem[:i] + self.mask[i] + mem[i + 1:]
        print(mem)
        self.mems[mem_key] = mem

    def decode(self, mem_key, mem_value):
        try:
            mem, final_mask = self.mems[mem_value]
        except KeyError:
            mem = "000000000000000000000000000000000000"
            final_mask = self.mask
        if mem_value == 0:
            bits = "000000000000000000000000000000000000"
        else:
            bits = "{0:b}".format(mem_value)
        #full_bits = "000000000000000000000000000000000000"
        #full_bits = full_bits[:len(full_bits) - len(bits)] + bits
        mem = mem[:len(mem) - len(bits)] + bits
        #for i in range(len(self.mask)):
        #    if self.mask[i] != 'X':
        #        mem = mem[:i] + self.mask[i] + mem[i + 1:]
        print('Decode')
        print(final_mask)
        print(mem)
        self.recursive(final_mask, -1, int_to_bits(mem_key), int(mem, 2))
        self.mems[mem_key] = (mem, final_mask)

    def final_decode(self):
        sums = 0
        for mem, final_mask in self.mems.items():
            mem_val = final_mask[0]
            final_mask = final_mask[1]
            print('*****')
            print(int(mem_val, 2))
            bits = "{0:b}".format(mem)
            mem = "000000000000000000000000000000000000"
            mem = mem[:len(mem) - len(bits)] + bits
            print(mem)
            print(int(mem, 2))
            for i in range(len(final_mask)):
                if final_mask[i] == '1':
                    mem = mem[:i] + str(1) + mem[i + 1:]

            print(final_mask)
            for i in range(len(final_mask)):
                if final_mask[i] == 'X':
                    final_mask = final_mask[:i] + str(0) + final_mask[i + 1:]
                    mem_a = mem[:i] + str(0) + mem[i + 1:]
                    val_a = self.recursive(final_mask, i, mem_a, mem_val)
                    mem_b = mem[:i] + str(1) + mem[i + 1:]
                    val_b = self.recursive(final_mask, i, mem_b, mem_val)
                    sums += val_a + val_b
                    break
        return sums

    def recursive(self, final_mask, i, mem, value):
        for j in range(i + 1, len(final_mask)):
            if final_mask[j] == 'X':
                final_mask = final_mask[:j] + str(0) + final_mask[j + 1:]
                mem_a = mem[:j] + str(0) + mem[j + 1:]
                val_a = self.recursive(final_mask, j, mem_a, value)
                mem_b = mem[:j] + str(1) + mem[j + 1:]
                val_b = self.recursive(final_mask, j, mem_b, value)
                return val_a + val_b
            elif final_mask[j] == '1':
                mem = mem[:j] + str(1) + mem[j + 1:]

        self.values.append(int(mem, 2))
        self.bits.append(mem)
        print('SETTING MEM:' + str(int(mem, 2)) + ', TO VALUE:' + str(value))
        self.decode_mems[int(mem, 2)] = value
        return int(mem, 2)

    def mem_to_int(self):
        return int(self.mem, 2)


mask = Mask()
mask.set_var('mems', {})
mask.set_var('mem', str("000000000000000000000000000000000000"))

part_1 = False
part_2 = True

if part_1:
    for value in values:
        parts = value.split(' ')
        if parts[0] == 'mask':
            mask.set_var('mask', parts[-1])
        else:
            key = int((parts[0].split(']')[0]).split('[')[1])
            value = int(parts[-1])
            mask.add_new_med(key, value)

    summ = 0

    print(mask)
    for mem in mask.mems.values():
        val = int(mem, 2)
        summ += val
        print(val)


    print('FINAL')
    print(summ)

if part_2:
    mask.set_var('values', [])
    mask.set_var('bits', [])
    mask.set_var('decode_mems', {})
    for value in values:
        parts = value.split(' ')
        if parts[0] == 'mask':
            mask.set_var('mask', parts[-1])
        else:
            key = int((parts[0].split(']')[0]).split('[')[1])
            value = int(parts[-1])
            mask.decode(key, value)

    print('FINAL')
    #result = mask.final_decode()
    print('NEW')
    sums = 0
    for key, mem_val in mask.decode_mems.items():
        sums += mem_val
    print('FINAL')
    print(sums)
