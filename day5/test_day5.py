import pytest

from problem import decode_row, decode_seat, encode_id


@pytest.mark.parametrize('code,row', [
    ('FBFBBFFRLR', 44),
    ('BFFFBBFRRR', 70),
    ('FFFBBBFRRR', 14),
    ('BBFFBBFRLL', 102),
])
def test_day5_decode_row(code, row):
    assert decode_row(code) == row


@pytest.mark.parametrize('code,seat', [
    ('FBFBBFFRLR', 5),
    ('BFFFBBFRRR', 7),
    ('FFFBBBFRRR', 7),
    ('BBFFBBFRLL', 4),
])
def test_day5_decode_seat(code, seat):
    assert decode_seat(code) == seat


@pytest.mark.parametrize('row,seat,id', [
    (44, 5, 357),
    (70, 7, 567),
    (14, 7, 119),
    (102, 4, 820),
])
def test_day5_encode_id(row, seat, id):
    assert encode_id(row, seat) == id
