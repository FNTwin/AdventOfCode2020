import pytest
import collections


def read_data(path: str) -> str:
    with open(path, "r") as f:
        data = f.read()
    return data


def valid_pssws(data: str) -> int:
    valid_pssw = 0
    for line in data.splitlines():
        num, cond, pssw = line.split()
        cond = cond.replace(":", "")
        num_cond = num.split('-')
        num_start, num_end = int(num_cond[0]), int(num_cond[1])
        value = collections.Counter(pssw)[cond]
        if (value >= num_start) and (value <= num_end):
            valid_pssw += 1
    return valid_pssw


def valid_pssws_part2(data: str) -> int:
    valid_pssw = 0
    for line in data.splitlines():
        num, cond, pssw = line.split()
        cond = cond.replace(":", "")
        num_cond = num.split('-')
        num_start, num_end = int(num_cond[0]), int(num_cond[1])
        tmp = collections.deque(pssw)
        if (tmp[num_start - 1] == cond) ^ (tmp[num_end - 1] == cond):
            valid_pssw += 1
    return valid_pssw


test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [test_input, 2],
    )
)
def test_pssws_part1(input: str, result: int):
    assert valid_pssws(input) == result


test_input = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [test_input, 1],
    )
)
def test_pssws_part2(input: str, result: int):
    assert valid_pssws_part2(input) == result


def main():
    input = "input.txt"
    part1 = valid_pssws(read_data(input))
    print("Part 1 solution: ", part1)
    part2 = valid_pssws_part2(read_data(input))
    print("Part 2 solution: ", part2)


if __name__ == "__main__":
    main()
