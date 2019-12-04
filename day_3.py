from math import sqrt, pow


def move_right(position):
    return position[0], position[1] + 1


def move_left(position):
    return position[0], position[1] - 1


def move_up(position):
    return position[0] + 1, position[1]


def move_down(position):
    return position[0] - 1, position[1]


moves = {
    'R': move_right,
    'L': move_left,
    'U': move_up,
    'D': move_down
}


def process_paths(paths):
    positions = [(0, 0)]

    for path in paths:
        for i in range(path[1]):
            positions.append(moves[path[0]](positions[-1]))

    return set(positions) - {(0, 0)}


def parse_path(path):
    return path[0], int(path[1:])


def find_crossings(wire_a, wire_b):
    path_a = process_paths([parse_path(p) for p in wire_a])
    path_b = process_paths([parse_path(p) for p in wire_b])

    return list(path_a.intersection(path_b))


def compute_distance(point):
    return abs(point[0]) + abs(point[1])


def find_closest_crossing(wire_a, wire_b):
    crossings = find_crossings(wire_a, wire_b)

    return min([compute_distance(c) for c in crossings])


if __name__ == '__main__':
    wires = []
    with open('./inputs/day_3.txt') as f:
        for wire in f:
            wires.append(wire.strip('\n'))

    wire_a = wires[0].split(',')
    wire_b = wires[1].split(',')

    print(find_closest_crossing(wire_a, wire_b))
