from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("src/counter.py", "Python") == 1639
    assert count_ocurrences("src/counter.py", "Javascript") == 122
