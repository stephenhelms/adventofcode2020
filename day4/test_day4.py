import pytest

from problem import count_valid_passports, parse_dataset, validate_passport_problem1,\
    validate_passport_problem2, VALIDATION_RULES

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

INVALID_PASSPORTS = """\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007\
"""
VALID_PASSPORTS = """\
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719\
"""


def test_day4_problem1_solve():
    passports = list(parse_dataset(DATASET))
    assert count_valid_passports(passports, validate_passport_problem1) == 2


def test_day4_parse_dataset():
    passports = list(parse_dataset(DATASET))
    assert len(passports) == 4
    assert set(passports[0].keys()) == {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt'}


@pytest.mark.parametrize('field,value,is_valid', [
    ('byr', 2002, True),
    ('byr', 2003, False),
    ('hgt', '60in', True),
    ('hgt', '190cm', True),
    ('hgt', '190in', False),
    ('hgt', '190', False),
    ('hcl', '#123abc', True),
    ('hcl', '#123abz', False),
    ('hcl', '123abc', False),
    ('ecl', 'brn', True),
    ('ecl', 'wat', False),
    ('pid', '000000001', True),
    ('pid', '0123456789', False),
])
def test_day4_problem2_validation_inputs(field, value, is_valid):
    assert bool(VALIDATION_RULES[field](str(value))) == is_valid


def test_day4_problem2_passport_validation():
    invalid_passports = list(parse_dataset(INVALID_PASSPORTS))
    assert not any(validate_passport_problem2(passport) for passport in invalid_passports)

    valid_passports = list(parse_dataset(VALID_PASSPORTS))
    assert all(validate_passport_problem2(passport) for passport in valid_passports)
