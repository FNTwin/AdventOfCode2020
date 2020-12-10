from collections import Counter, defaultdict


def read(path):
    with open(path, "r") as f:
        return f.read()


def parse(data):
    data = [int(i) for i in data.split("\n")]
    return data


def part_1(data):
    socket = 0
    count = Counter()
    for value in data:
        count[value - socket] += 1
        socket = value
    return count[1] * count[3]


def part_2(data):
    adaptors = defaultdict(int)
    adaptors[0] = 1
    for value in data:
        adaptors[value] = adaptors[value - 1] + \
                          adaptors[value - 2] + \
                          adaptors[value - 3]
    return adaptors[data[-1]]


def main():
    path = "input.txt"
    data = parse(read(path))
    target = max(data) + 3
    data.append(target)
    data.sort()
    print("Part 1 solution: ", part_1(data))
    print("Part 2 solution: ", part_2(data))


if __name__ == "__main__":
    main()
