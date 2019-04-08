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
import re

_MOBILE_PHONE_PATTERN = '(\+7|8|)(7|9)([0-9]{9})'
  
def is_mobile_phone(number):
    # pattern = re.compile(_MOBILE_PHONE_PATTERN)
    number = clear_number(number)
    return bool(re.match(_MOBILE_PHONE_PATTERN, number))


def clear_number(number):
    symbol_list = [symbol for symbol in number if symbol in '+0123456789']
    return ''.join(symbol_list)

