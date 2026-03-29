from rule_engine.rule_executor import execute_rule
from rule_engine.rule_parser import parse_rule


EXAMPLE_1 = {
    "credit_rating": 75,
    "flood_risk": 5,
    "revenue": 1000
}

RULE = """
credit_rating is above 50
AND
flood_risk is below 10
OR
revenue is above 1000000
"""

# RULE = "revenue is above 1000000"

# RULE = """
# revenue is above 1000000
# AND
# flood_risk is below 5
# """

# RULE = """
# (
#     revenue is above 1000000
#     AND
#     flood_risk is above 4
# )
# OR
# (
#     revenue is below 1500
#     AND
#     flood_risk is below or equals 5
#     AND
#     credit_rating is above 50
# )
# """


def evaluate(rule, data):
    rule_tree = parse_rule(rule)

    return execute_rule(rule_tree, data)


print(evaluate(RULE, EXAMPLE_1))
