from module import even
fixtures = [
    (
        (1,2,3,4,5,6),
        (2,4,6)
    ),
    (
        (2,11,13,15,17,18,21),
        (2,18)
    ),
    ((2,11,14,11,15,17,19,2,14,2),(2,14)),
    ((2,'22443*',14,11,15,17,19,2,14,2),(2,14)),
]

def test_even():
    for inputted, expected  in fixtures:
        assert even(*inputted) == expected