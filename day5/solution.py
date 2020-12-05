import pytest


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return data


def parse_input_decodify(data):
    lines = data.splitlines()
    decode_row = lambda x: "1" if x == "B" else "0"
    decode_column = lambda x: "1" if x == "R" else "0"
    l = []
    for line in lines:
        r = line[:7]
        c = line[7:]
        r = "".join([decode_row(i) for i in r])
        c = "".join([decode_column(i) for i in c])
        decimal_r, decimal_c = int(r, 2), int(c, 2)
        l.append(decimal_r * 8 + decimal_c)
    l.sort()
    return l[-1]


def parse_input_decodify_2(data):
    lines = data.splitlines()
    decode_row = lambda x: "1" if x == "B" else "0"
    decode_column = lambda x: "1" if x == "R" else "0"
    max_number = 2 ** 10
    all_seats = [i for i in range(max_number)]
    for line in lines:
        r = line[:7]
        c = line[7:]
        r = "".join([decode_row(i) for i in r])
        c = "".join([decode_column(i) for i in c])
        binary_seat = r + c
        try:
            all_seats.remove(int(binary_seat, 2))
        except ValueError:
            pass
    for seat in all_seats:
        if seat - 1 not in all_seats and seat + 1 not in all_seats:
            return seat


input_1 = "FBFBBFFRLR"


@pytest.mark.parametrize(
    ("input", "result"), (
            [input_1, 357],
    )
)
def test_part1(input, result):
    assert parse_input_decodify(input) == result


def main():
    path = "input.txt"
    print("Part 1 solution: ", parse_input_decodify(read(path)))
    print("Part 2 solution: ", parse_input_decodify_2(read(path)))


if __name__ == "__main__":
    main()
