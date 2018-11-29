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
)
]

for inputted, expected in fixtures:
	print(inputted, ' * ', expected)

def test_even():
    for inputted, expected  in fixtures:
        assert even(*inputted) == expected