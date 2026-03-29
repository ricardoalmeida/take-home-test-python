
import unittest
from unittest.mock import patch


class TestRuleParser(unittest.TestCase):
    def setUp(self) -> None:
        self.patcher = patch(
            'rule_engine.rule_parser.parse_statement',
            side_effect=lambda value: value
        )
        self.patcher.start()

        from rule_engine.rule_parser import parse_rule
        self.parse_rule = parse_rule

        return super().setUp()

    def tearDown(self) -> None:
        self.patcher.stop()
        return super().tearDown()

    def test_simple_and_rule(self):
        rule = """\
score is above 50
AND
score is below 100
"""
        expected = {
            "operator": "AND",
            "left_operand": "score is above 50",
            "right_operand": "score is below 100"
        }

        self.assertEqual(expected, self.parse_rule(rule))

    def test_simple_or_rule(self):
        rule = """\
score is below 50
OR
score is above 100
"""
        expected = {
            "operator": "OR",
            "left_operand": "score is below 50",
            "right_operand": "score is above 100"
        }

        self.assertEqual(expected, self.parse_rule(rule))

    def test_complex_and_or_rule(self):
        rule = """\
score is below 50
AND
score is above 100
OR
score is equal 0
"""
        expected = {
            "operator": "OR",
            "right_operand": "score is equal 0",
            "left_operand": {
                "operator": "AND",
                "left_operand": "score is below 50",
                "right_operand": "score is above 100"
            }
        }

        self.assertEqual(expected, self.parse_rule(rule))

    def test_rule_with_parentheses(self):
        rule = """\
(
    score is below 50
    OR
    score is above 100
)
AND
(
    risk is below 10
    OR
    value is below 1000
)

"""
        expected = {
            "operator": "AND",
            "left_operand": {
                "operator": "OR",
                "left_operand": "score is below 50",
                "right_operand": "score is above 100"
            },
            "right_operand": {
                "operator": "OR",
                "left_operand": "risk is below 10",
                "right_operand": "value is below 1000"
            }
        }

        self.assertEqual(expected, self.parse_rule(rule))

    def test_complex_rule_with_parentheses(self):
        rule = """\
(
    score is below 50
    OR
    score is above 100
)
AND
(
    risk is below 10
    OR
    value is below 1000
    OR
    credit_rating is above 23
)

"""
        expected = {
            "operator": "AND",
            "left_operand": {
                "operator": "OR",
                "left_operand": "score is below 50",
                "right_operand": "score is above 100"
            },
            "right_operand": {
                "operator": "OR",
                "left_operand": "risk is below 10",
                "right_operand": {
                    "operator": "OR",
                    "left_operand": "value is below 1000",
                    "right_operand": "credit_rating is above 23",
                }
            }
        }

        self.assertEqual(expected, self.parse_rule(rule))


if __name__ == '__main__':
    unittest.main()
