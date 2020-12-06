import pytest


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return data


def ride(input):
    tree, x, y = 0, 0, 0
    lines = input.splitlines()
    while y < (len(lines) - 1):
        x += 3
        y += 1
        x %= len(lines[0])
        if lines[y][x] == "#":
            tree += 1
    return tree


def minimal_ride(input, mode_number, modes=None):
    tree, x, y = 0, 0, 0
    lines = input.splitlines()
    while y < (len(lines) - 1):
        x += modes[mode_number]["x"]
        y += modes[mode_number]["y"]
        x %= len(lines[0])
        if lines[y][x] == "#":
            tree += 1
    return tree


pattern = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [pattern, 7],
    )
)
def test_ride(input, result):
    assert ride(input) == result


@pytest.mark.parametrize(
    ("input", "result"), (
            [pattern, 336],
    )
)
def test_minimal_ride(input, result):
    modes = {
        "1": {"x": 1, "y": 1},
        "2": {"x": 3, "y": 1},
        "3": {"x": 5, "y": 1},
        "4": {"x": 7, "y": 1},
        "5": {"x": 1, "y": 2},
    }

    prod = 1
    l = []
    for i in range(1, 6):
        l.append(minimal_ride(input, str(i), modes))
        prod *= l[i - 1]
    assert prod == result


def main():
    path = "input.txt"
    input = read(path)
    print("Part 1 solution: ", ride(input))

    modes = {
        "1": {"x": 1, "y": 1},
        "2": {"x": 3, "y": 1},
        "3": {"x": 5, "y": 1},
        "4": {"x": 7, "y": 1},
        "5": {"x": 1, "y": 2},
    }

    prod = 1
    l = []
    for i in range(1, 6):
        l.append(minimal_ride(input, str(i), modes))
        prod *= l[i - 1]
    print("Part 2 solution: ", prod)


if __name__ == "__main__":
    main()
