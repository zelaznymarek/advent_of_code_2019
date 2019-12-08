from day_8_part_1 import split_to_layers, PIXELS_PER_LAYER, COLS


def process(digits):
    layers = split_to_layers(digits, PIXELS_PER_LAYER)
    base_layer = layers.pop()

    for layer in layers[::-1]:
        base_layer = add_layer(layer, base_layer, PIXELS_PER_LAYER)

    image = split_to_layers(base_layer, COLS)

    for row in image:
        print(row)


def add_layer(layer, base_layer, layer_size):
    for i in range(layer_size):
        pixel = layer[i]
        if pixel != 2:
            base_layer[i] = pixel

    return base_layer


if __name__ == '__main__':
    with open('./inputs/day_8.txt') as f:
        digits = [int(char) for char in list(f.readline())]

    process(digits)
