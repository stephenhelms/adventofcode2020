from problem import count_valid_passports, parse_dataset, validate_passport_problem1, VALIDATION_RULES

DATASET = """\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in\
"""


def test_day4_problem1_solve():
    passports = list(parse_dataset(DATASET))
    assert count_valid_passports(passports, validate_passport_problem1) == 2


def test_day4_parse_dataset():
    passports = list(parse_dataset(DATASET))
    assert len(passports) == 4
    assert set(passports[0].keys()) == {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}
