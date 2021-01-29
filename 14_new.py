from Utils import read_values

values = read_values('14_value', split_on=" ")


def replace_first_x(mask):
    mask_a = mask.replace('X', '0', 1)
    mask_b = mask.replace('X', '1', 1)
    return mask_a, mask_b


def make_sub_masks(mask):
    dirty_mask = [mask]
    clean_mask = []

    while len(dirty_mask) > 0:
        mask_to_clean = dirty_mask.pop()
        a_mask, b_mask = replace_first_x(mask_to_clean)
        if 'X' in a_mask:
            dirty_mask.append(a_mask)
            dirty_mask.append(b_mask)
        else:
            clean_mask.append(a_mask)
            clean_mask.append(b_mask)

    return clean_mask


def bit_to_int(value):
    return int(value, 2)


def int_to_bit(value):
    bits = "000000000000000000000000000000000000"
    int_val = "{0:b}".format(value)
    return bits[:len(bits) - len(int_val)] + int_val


def get_mem_key(value):
    return int(value.replace('mem[', '').replace(']', ''))


def get_key(mask, value):
    new_key = ''

    for i in range(len(mask)):
        if mask[i] == '1':
            new_key += '1'
        elif mask[i] == 'X':
            new_key += 'X'
        else:
            new_key += value[i]

    return new_key

masks = []
mems = {}
mask = None
for parts in values:
    if parts[0] == 'mask':
        mask = parts[2]
    else:
        result = get_key(mask, int_to_bit(int(get_mem_key(parts[0]))))
        masks = make_sub_masks(result)
        m_value = int(parts[2])
        for m in masks:
            m = bit_to_int(m)
            mems[m] = m_value

sums = 0
for val in mems.values():
    sums += val

print(sums)

