from years_7 import is_leap

YEARS = (
	(2000, True)
	(2016, True)
	(2018, False)
	(2019, False)
	(2020, True)
	)
def test_is_leap():
    for year in YEARS:
        assert is_leap(year[0]) == year[1]