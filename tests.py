from day_1 import additional_fuel, count_fuel, count_module_fuel, count_total_fuel
from day_2 import process_program
from day_3_part_1 import process_paths, parse_path, find_crossings, find_closest_crossing
from day_3_part_2 import count_moves, find_first_crossing
from day_4 import int_to_digits, is_possible, has_valid_adjacent_digits

tests = []


def add_test(func):
    tests.append(func)
    print(f'Added {func.__name__}')

    return func


# day 1


@add_test
def test_additional_fuel():
    fuel_mass = 33583

    expected = 16763

    return additional_fuel(fuel_mass) == expected


@add_test
def test_count_fuel():
    mass = 1969

    expected = 654

    return count_fuel(mass) == expected


@add_test
def test_count_module_fuel():
    module_mass = 100756

    expected = 50346

    return count_module_fuel(module_mass) == expected


@add_test
def test_count_total_fuel():
    modules = [100, 200, 300, 400]

    expected = 446

    return count_total_fuel(modules) == expected


# day 2


@add_test
def test_process_program():
    program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]

    expected = 3500

    return process_program(program) == expected


# day 3 part 1


@add_test
def test_process_paths():
    paths = [('R', 3), ('D', 1), ('L', 2), ('U', 3)]

    expected = [(0, 1), (0, 2), (0, 3), (-1, 3), (-1, 2), (-1, 1), (0, 1), (1, 1), (2, 1)]

    return process_paths(paths) == expected


@add_test
def test_parse_path():
    path = ['R3', 'U51', 'D7']

    expected = [('R', 3), ('U', 51), ('D', 7)]

    return [parse_path(p) for p in path] == expected


@add_test
def test_find_crossings():
    path_a = [(1, 0), (2, 0), (2, 1), (2, 2)]
    path_b = [(0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]

    expected = [(2, 1)]

    return find_crossings(path_a, path_b) == expected


@add_test
def test_find_closest_distance():
    wire_a = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire_b = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    expected = 159

    return find_closest_crossing(wire_a, wire_b) == expected

# day 3 part 2


@add_test
def test_count_moves():
    path_a = [(1, 0), (2, 0), (2, 1), (2, 2)]
    path_b = [(0, 1), (1, 1), (2, 1), (3, 1), (3, 2)]
    crossing = (2, 1)

    expected = 6

    return count_moves(path_a, path_b, crossing) == expected


@add_test
def test_find_first_crossing():
    wire_a = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire_b = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    expected = 610

    return find_first_crossing(wire_a, wire_b) == expected


# day 4


@add_test
def test_int_to_digits():
    number = 345764
    expected = [3, 4, 5, 7, 6, 4]

    return int_to_digits(number) == expected


@add_test
def test_is_possible():
    numbers = [111111, 223450, 123789, 112233, 123444, 111122]

    expected = [False, False, False, True, False, True]

    return [is_possible(number) for number in numbers] == expected


@add_test
def test_has_valid_adjacent_digits():
    numbers = [
        [1, 1, 1, 1, 1, 1],
        [2, 2, 3, 4, 5, 0],
        [1, 2, 3, 7, 8, 9],
        [1, 1, 2, 2, 3, 3],
        [1, 2, 3, 4, 4, 4],
        [1, 1, 1, 1, 2, 2],
        [1, 2, 2, 2, 3, 3]
    ]

    expected = [False, True, False, True, False, True, True]

    return [has_valid_adjacent_digits(number) for number in numbers] == expected


if __name__ == '__main__':
    print(f'\nGathered {len(tests)} tests.\n')

    for test in tests:
        result = 'passed' if test() else 'failed'

        print(f'{test.__name__} => {result}')
