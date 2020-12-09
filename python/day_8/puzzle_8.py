import re

with open("./day_8/data.txt") as f:
    instructions = f.read().splitlines()


def execute(instructions: [str]):
    acc = 0
    ip = 0
    visited_ip = set()

    while ip < len(instructions) and ip not in visited_ip:
        instruction = instructions[ip]
        visited_ip.add(ip)

        op, param = instruction.split()
        param = int(param)

        if op == 'jmp':
            ip += param
            continue

        if op == 'acc':
            acc += param
        elif op == 'nop':
            pass
        else:
            raise RuntimeError()
        
        ip += 1

    return acc


result = execute(instructions)
print('Accumulator after loop detection', result)

