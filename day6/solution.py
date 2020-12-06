import pytest


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return data


def count_answers(input):
    n = 0
    lines = input.split("\n\n")
    for line in lines:
        unique = (set(line) - set("\n"))
        n += len(unique)
    return n


def count_answers_2(input):
    n = 0
    lines = input.split("\n\n")
    for group in lines:
        group = group.splitlines()
        unique = set(group[0])
        for answer in group[1:]:
            unique = unique.intersection(answer)  # intersection can also be use with unique &= answer
        n += len(unique)
    return n


pattern = """abc

a
b
c

ab
ac

a
a
a
a

b
"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [pattern, 11],
    )
)
def test_part_1(input, result):
    assert count_answers(input) == result


@pytest.mark.parametrize(
    ("input", "result"), (
            [pattern, 6],
    )
)
def test_part_2(input, result):
    assert count_answers_2(input) == result


def main():
    path = "input.txt"
    data = read(path)
    print("Part 1 solution: ", count_answers(data))
    print("Part 2 solution: ", count_answers_2(data))


if __name__ == "__main__":
    main()
