from collections import Counter
from datetime import datetime


def has_valid_adjacent_digits(digits):
    digit_counter = Counter(digits)

    return 2 in digit_counter.values()


def int_to_digits(number):
    return list(map(int, list(str(number))))


def is_possible(password):
    digits = int_to_digits(password)

    _has_valid_adjacent_digits = has_valid_adjacent_digits(digits)

    if sorted(digits) != digits:
        return False

    return _has_valid_adjacent_digits


def count_possible_passwords(start, end):
    possible_passwords = 0

    for i in range(start, end + 1):
        if is_possible(i):
            possible_passwords += 1

    return possible_passwords


if __name__ == '__main__':
    with open('./inputs/day_4.txt') as f:
        start, end = list(map(int, f.readline().split('-')))

    print(count_possible_passwords(start, end))
