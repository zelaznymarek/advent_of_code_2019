from collections import Counter

COLS = 25
ROWS = 6
PIXELS_PER_LAYER = COLS * ROWS


def process(digits):
    layers = split_to_layers(digits, PIXELS_PER_LAYER)

    counted = [Counter(layer) for layer in layers]

    layer_with_min_zeros = get_layer_with_min_zeros(counted)

    return layer_with_min_zeros[1] * layer_with_min_zeros[2]


def split_to_layers(digits, layer_size):
    layers = []
    layers_number = int(len(digits) / layer_size)

    for i in range(layers_number):
        start = i * layer_size
        end = (i + 1) * layer_size
        layer = digits[start:end]
        layers.append(layer)

    return layers


def get_layer_with_min_zeros(layer_counters):
    sorted_by_zeros = sorted(layer_counters, key=lambda x: x[0])

    return sorted_by_zeros[0]


if __name__ == '__main__':
    with open('./inputs/day_8.txt') as f:
        digits = [int(char) for char in list(f.readline())]

    print(process(digits))
