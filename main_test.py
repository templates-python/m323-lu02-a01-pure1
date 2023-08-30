import main
def test_sum_positive_numbers(self):
    """Testfall für eine Liste von positiven Zahlen."""
    self.assertEqual(main.sum_of_numbers([1, 2, 3, 4, 5]), 15)

def test_sum_mixed_numbers(self):
    """Testfall für eine Liste von gemischten Zahlen (positiv und negativ)."""
    self.assertEqual(main.sum_of_numbers([1, -1, 2, -2]), 0)

def test_sum_single_number(self):
    """Testfall für eine Liste mit einer einzigen Zahl."""
    self.assertEqual(main.sum_of_numbers([7]), 7)

def test_sum_empty_list(self):
    """Testfall für eine leere Liste."""
    self.assertEqual(main.sum_of_numbers([]), 0)