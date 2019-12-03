from day_1 import additional_fuel, count_fuel, count_module_fuel, count_total_fuel
from day_2 import process_program

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


if __name__ == '__main__':
    print(f'\nGathered {len(tests)} tests.\n')

    for test in tests:
        result = 'passed' if test() else 'failed'

        print(f'{test.__name__} => {result}')
