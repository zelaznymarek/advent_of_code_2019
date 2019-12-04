from day_1 import additional_fuel, count_fuel, count_module_fuel, count_total_fuel
from day_2 import process_program
from day_3 import process_paths, parse_path, find_crossings, find_closest_crossing

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


# day 3


@add_test
def test_process_paths():
    paths = [('R', 3), ('D', 1), ('L', 2), ('U', 3)]
    expected = {(0, 0), (0, 1), (0, 2), (0, 3), (-1, 3), (-1, 2), (-1, 1), (1, 1), (2, 1)}

    return process_paths(paths) == expected


@add_test
def test_parse_path():
    path = ['R3', 'U51', 'D7']
    expected = [('R', 3), ('U', 51), ('D', 7)]

    return [parse_path(p) for p in path] == expected


@add_test
def test_find_crossings():
    wire_a = ['R2', 'U7']
    wire_b = ['U3', 'R5']
    expected = [(3, 2)]

    return find_crossings(wire_a, wire_b) == expected


@add_test
def test_find_closest_distance():
    wire_a = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    wire_b = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']
    expected = 159

    return find_closest_crossing(wire_a, wire_b) == expected


if __name__ == '__main__':
    print(f'\nGathered {len(tests)} tests.\n')

    for test in tests:
        result = 'passed' if test() else 'failed'

        print(f'{test.__name__} => {result}')
