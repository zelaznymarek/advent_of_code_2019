from day_3_part_1 import find_crossings, process_paths, parse_path


def count_moves(path_a, path_b, crossing):
        moves_in_path_a = path_a.index(crossing) + 1
        moves_in_path_b = path_b.index(crossing) + 1

        return moves_in_path_a + moves_in_path_b


def find_first_crossing(wire_a, wire_b):
    path_a = process_paths([parse_path(p) for p in wire_a])
    path_b = process_paths([parse_path(p) for p in wire_b])

    crossings = find_crossings(path_a, path_b)

    return min([count_moves(path_a, path_b, crossing) for crossing in crossings])


if __name__ == '__main__':
    wires = []
    with open('./inputs/day_3.txt') as f:
        for wire in f:
            wires.append(wire.strip('\n'))

    wire_a = wires[0].split(',')
    wire_b = wires[1].split(',')

    print(find_first_crossing(wire_a, wire_b))
