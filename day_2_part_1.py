def process_program(program):
    for i in range(0, len(program), 4):
        opcode, op_1, op_2, result = tuple(program[i:i+4])

        if opcode == 99:
            return program[0]
        elif opcode == 1:
            program[result] = program[op_1] + program[op_2]
        elif opcode == 2:
            program[result] = program[op_1] * program[op_2]


def restore_gsp(program):
    program[1] = 12
    program[2] = 2

    return program


if __name__ == '__main__':
    program = list(map(int, input().split(',')))

    restored = restore_gsp(program)

    print(process_program(restored))
