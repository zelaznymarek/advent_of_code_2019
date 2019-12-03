def adjust_params(program):
    for i in range(100):
        for j in range(100):
            program_copy = program[:]
            program_copy[1] = i
            program_copy[2] = j

            if process_program(program_copy) == 19690720:
                return 100 * i + j


def process_program(program):
    for i in range(0, len(program), 4):
        if program[i] == 99:
            return program[0]

        opcode, param_1, param_2, result = tuple(program[i:i+4])

        if opcode == 1:
            program[result] = program[param_1] + program[param_2]
        else:
            program[result] = program[param_1] * program[param_2]


if __name__ == '__main__':
    program = list(map(int, input().split(',')))

    print(adjust_params(program))
