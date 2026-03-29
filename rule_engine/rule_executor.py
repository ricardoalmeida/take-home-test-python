def execute_rule(rule, data):
    match(rule["operator"]):
        case "AND":
            return execute_rule(rule["left_operand"], data) and execute_rule(rule["right_operand"], data)
        case "OR":
            return execute_rule(rule["left_operand"], data) or execute_rule(rule["right_operand"], data)
        case "gte" | "nlt":
            return data[rule["field"]] >= rule["value"]
        case "lte" | "ngt":
            return data[rule["field"]] <= rule["value"]
        case "e":
            return data[rule["field"]] == rule["value"]
        case "ne":
            return data[rule["field"]] != rule["value"]
        case "gt" | "nlte":
            return data[rule["field"]] > rule["value"]
        case "lt" | "ngte":
            return data[rule["field"]] < rule["value"]
