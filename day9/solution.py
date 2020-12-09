import pytest


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return [int(i) for i in data.split("\n")]


def twoSum_bool(nums, target):
    m = {}
    for i in range(len(nums)):
        m[nums[i]] = i

    for i in range(len(nums)):
        res = target - nums[i]
        if (res in m) and (m[res] != i):
            return False
    return True


def search_part_1(input, preamble):
    for i in range(0, len(input)):
        if i >= preamble:
            array = input[i - preamble:i]
            if twoSum_bool(array, input[i]):
                return input[i], i


def search_part_2(input, pos, value):
    array = input[:pos]
    tmp = []
    for i in range(len(array)):
        tmp.append(input[i])
        for j in range(i, len(array)):
            if sum(tmp) < value:
                tmp.append(input[j])
            elif sum(tmp) == value:
                return min(tmp) + max(tmp)
            else:
                tmp = []


input_test = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


@pytest.mark.parametrize(
    ('input', 'result'),
    (
            [input_test, 127],
    ),
)
def test_part1(input, result):
    input = [int(i) for i in input.split("\n")]
    assert search_part_1(input, 5)[0] == result


@pytest.mark.parametrize(
    ('input', 'result'),
    (
            [input_test, 62],
    ),
)
def test_part2(input, result):
    input = [int(i) for i in input.split("\n")]
    value, pos = search_part_1(input, 5)
    assert search_part_2(input, pos, value) == result


def main():
    path = "input.txt"
    data = read(path)
    preamble = 25
    value, pos = search_part_1(data, preamble)
    print("Solution Part 1: ", value)
    print("Solution Part 2: ", search_part_2(data, pos, value))


if __name__ == "__main__":
    main()
