def read(path):
    with open(path, "r") as f:
        return f.read()


def parse_input(data):
    lines = data.splitlines()
    commands = []
    for line in lines:
        line = line.split()
        commands.append([line[0], int(line[1])])
    return commands


def loop(commands):
    pos = 0
    n = 0
    unique = set()
    while pos not in unique and pos < len(commands):
        unique.add(pos)
        if commands[pos][0] == "acc":
            n += commands[pos][1]
            pos += 1
        elif commands[pos][0] == "jmp":
            pos += commands[pos][1]
        else:
            pos += 1
    return n, pos


def loop2(commands):
    for i, (cmd, value) in enumerate(commands):
        if cmd == 'acc':
            continue
        flip_command = {'jmp': 'nop', 'nop': 'jmp'}
        new_commands = commands.copy()
        new_commands[i] = [flip_command[cmd], value]
        acc, pos = loop(new_commands)
        if pos == len(commands):
            return acc


def main():
    path = "input.txt"
    commands = parse_input(read(path))
    print("Part 1 solution: ", loop(commands)[0])
    print("Part 2 solution: ", loop2(commands))


if __name__ == "__main__":
    main()
