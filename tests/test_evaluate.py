import unittest

from index import evaluate


EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}


class TestEvaluate(unittest.TestCase):

    def test_challenge_rule_with_example_1(self):
        """The specific rule from the challenge should return True for EXAMPLE_1."""
        rule = """
credit_rating is above 50
AND
flood_risk is below 10
OR
revenue is above 1000000
"""
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_simple_true(self):
        rule = "credit_rating is above 50"
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_simple_false(self):
        rule = "revenue is above 1000000"
        self.assertFalse(evaluate(rule, EXAMPLE_1))

    def test_and_both_true(self):
        rule = """
credit_rating is above 50
AND
flood_risk is below 10
"""
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_and_one_false(self):
        rule = """
credit_rating is above 50
AND
revenue is above 1000000
"""
        self.assertFalse(evaluate(rule, EXAMPLE_1))

    def test_or_one_true(self):
        rule = """
credit_rating is above 50
OR
revenue is above 1000000
"""
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_or_both_false(self):
        rule = """
credit_rating is above 100
OR
revenue is above 1000000
"""
        self.assertFalse(evaluate(rule, EXAMPLE_1))

    def test_equals(self):
        rule = "flood_risk equals 5"
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_below_or_equals(self):
        rule = "flood_risk is below or equals 5"
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_above_or_equals(self):
        rule = "credit_rating is above or equals 75"
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_parentheses_grouping(self):
        """Parentheses override default AND-before-OR precedence."""
        rule = """
(
    revenue is above 1000000
    AND
    flood_risk is above 4
)
OR
(
    revenue is below 1500
    AND
    flood_risk is below or equals 5
    AND
    credit_rating is above 50
)
"""
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_not_operator(self):
        rule = "revenue is not above 1000000"
        self.assertTrue(evaluate(rule, EXAMPLE_1))

    def test_challenge_rule_false_data(self):
        """Credit_rating below 50, flood_risk above 10, revenue below 1000000 → False."""
        data = {
            "credit_rating": 30,
            "flood_risk": 15,
            "revenue": 500
        }
        rule = """
credit_rating is above 50
AND
flood_risk is below 10
OR
revenue is above 1000000
"""
        self.assertFalse(evaluate(rule, data))

    def test_challenge_rule_or_branch_true(self):
        """First group false, but revenue > 1000000 makes OR branch true."""
        data = {
            "credit_rating": 30,
            "flood_risk": 15,
            "revenue": 2000000
        }
        rule = """
credit_rating is above 50
AND
flood_risk is below 10
OR
revenue is above 1000000
"""
        self.assertTrue(evaluate(rule, data))


if __name__ == '__main__':
    unittest.main()
