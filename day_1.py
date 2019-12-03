from math import floor
from datetime import datetime


def additional_fuel(fuel_mass):
    fuel = count_fuel(fuel_mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + additional_fuel(fuel)


def count_fuel(mass):
    return floor(mass / 3) - 2


def count_module_fuel(module_mass):
    module_fuel = count_fuel(module_mass)
    additional = additional_fuel(module_fuel)

    return module_fuel + additional


def count_total_fuel(modules):
    total_fuel = 0

    for module in modules:
        total_fuel += count_module_fuel(module)

    return total_fuel


if __name__ == '__main__':
    modules = []
    while True:
        try:
            line = input()
            if line == '':
                break
        except EOFError:
            break
        modules.append(int(line))

    start = datetime.now().timestamp()
    print(count_total_fuel(modules))
    print(f'Time: {datetime.now().timestamp() - start} ms')
