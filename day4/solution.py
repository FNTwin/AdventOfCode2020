import pytest


def read(path):
    with open(path, "r") as f:
        data = f.read()
    return data


def parse_input_and_count(data, requirements):
    count = 0
    lines = data.split("\n\n")
    for passport_unformatted in lines:
        passports_list = [i.split(":") for i in passport_unformatted.split()]
        passport = {key: value for key, value in passports_list}
        if passport.keys() >= requirements:
            count += 1
    return count


def parse_input_and_count_2(data, requirements):
    count = 0
    lines = data.split("\n\n")
    for passport_unformatted in lines:
        passports_list = [i.split(":") for i in passport_unformatted.split()]
        passport = {key: value for key, value in passports_list}
        if passport.keys() >= requirements.keys():
            if check(passport, requirements):
                count += 1
    return count


def check(passport, requirements):
    if (requirements["byr"][0] <= int(passport["byr"]) <= requirements["byr"][1]
            and requirements["iyr"][0] <= int(passport["iyr"]) <= requirements["iyr"][1]
            and requirements["eyr"][0] <= int(passport["eyr"]) <= requirements["eyr"][1]
            and (((cond := str(passport["hgt"][-2:])) in requirements["hgt"]))
            and int(requirements["hgt"][cond][0]) <= int(
                ''.join(filter(lambda x: x.isdigit(), passport["hgt"]))) <= int(requirements["hgt"][cond][1])
            and (passport["hcl"][0] == "#")
            and sum([i in requirements["hcl"]["valid"] for i in passport["hcl"][1:]]) == int(requirements["hcl"]["num"])
            and (passport["ecl"] in requirements["ecl"])
            and (len(''.join(filter(lambda x: x.isdigit(), passport["pid"]))) == 9)
    ):
        return True
    else:
        return False


input_test = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [input_test, 2],
    )
)
def test_part1(input, result):
    required = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    assert parse_input_and_count(input, required) == result


input_test2 = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""


@pytest.mark.parametrize(
    ("input", "result"), (
            [input_test2, 4],
    )
)
def test_part2(input, result):
    required2 = {
        'byr': [1920, 2002],
        'iyr': [2010, 2020],
        'eyr': [2020, 2030],
        'hgt': {
            "cm": [150, 193],
            "in": [59, 76]
        },
        'hcl': {
            "num": 6,
            "valid": "abcdef0123456789",
        },
        'ecl': ["amb", "blu", "brn", "gry", "grn", "hzl", "oth" ],
        'pid': 9
    }
    assert parse_input_and_count_2(input, required2) == result


def main():
    required = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    required2 = {
        'byr': [1920, 2002],
        'iyr': [2010, 2020],
        'eyr': [2020, 2030],
        'hgt': {
            "cm": [150, 193],
            "in": [59, 76]
        },
        'hcl': {
            "num": 6,
            "valid": "abcdef0123456789",
        },
        'ecl': ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        'pid': 9
    }

    data = read("input.txt")
    print("Part 1 solution: ", parse_input_and_count(data, required))
    print("Part 2 solution: ", parse_input_and_count_2(data, required2))


if __name__ == "__main__":
    main()
