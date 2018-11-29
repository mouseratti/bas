from students.mkoshel.mobile_phones.mobile import is_mobile_phone
from students.mkoshel.mobile_phones.mobile import clear_number
"""
Из данного списка нужно отфильтровать все мобильные номера
(Начинаются с +79XXXXXXXXX либо 89XXXXXXXXX либо 77XXXXXXXXX 9XXXXXXXXX)
 +79236765X97 # no
 89136645101 # yes
 83812640423 # no
 8(904)541-02-03 #yes
 +1(555)345-11-21 # no
 +8(3812) 360-263 # no
 904-333-22-12 # yes
 9333026455 # yes
 +77715432100 yes
 +771222b3451 no
 +77172123456  yes
 +7-735-543-21-00 yes
 """

fixtures = [
    ('+79236765X97', False),
    ('89136645101', True),
    ('83812640423', False),
    ('8(904)541-02-03', True),
    ('+8(3812) 360-263', False),
    ('+1(555)345-11-21', False),
    ('904-333-22-12', True),
    ('9333026455', True),
    ('+77715432100', True),
    ('+771222b3451', False),
    ('+77172123456', True),
    ('+771222b3451', False),
    ('+7-735-543-21-00', True),
]

def test_is_mobile():
    for phone, is_mobile in fixtures:
        assert is_mobile_phone(phone) == is_mobile


def test_clear_number():
    for inputted, expected in [
        ('1-2-3', '123'),
        ('(12)3', '123'),
        ("+1(23)", '+123'),
        # ("+1(23)", '+123+'),
    ]:
        assert clear_number(inputted) == expected