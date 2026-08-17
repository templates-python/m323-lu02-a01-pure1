import main


def test_sum_positive_numbers():
    """Testfall für eine Liste von positiven Zahlen."""
    assert main.sum_of_numbers([1, 2, 3, 4, 5]) == 15


def test_sum_mixed_numbers():
    """Testfall für eine Liste von gemischten Zahlen (positiv und negativ)."""
    assert main.sum_of_numbers([1, -1, 2, -2]) == 0


def test_sum_single_number():
    """Testfall für eine Liste mit einer einzigen Zahl."""
    assert main.sum_of_numbers([7]) == 7


def test_sum_empty_list():
    """Testfall für eine leere Liste."""
    assert main.sum_of_numbers([]) == 0
