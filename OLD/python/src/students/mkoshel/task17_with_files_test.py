from task17_with_files import count_words
fixture = "three one two three two four three"

def test_count_words():
    result = count_words(fixture)
    assert isinstance(result, dict)
    assert result["one"] == 1
    assert result["two"] == 2
    assert result["three"] == 3