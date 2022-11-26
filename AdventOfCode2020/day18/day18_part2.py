from math import prod


with open("day18_input.txt", encoding="utf-8", mode="r") as f:
    input_data = f.readlines()


def evaluate_expression(expression):
    result = 0
    start = 0
    end = len(expression) - 1
    sub_expr = expression
    while True:
        if "(" not in sub_expr:
            groups = sub_expr.split(" * ")

            for index, item in enumerate(groups):
                groups[index] = sum([int(x) for x in item.split(" + ")])

            sub_result = prod(groups)

            expression = expression.replace("(" + sub_expr + ")", str(sub_result))
            if "(" not in expression:
                expression = expression.replace(sub_expr, str(sub_result))
            sub_expr = expression

        else:
            end = sub_expr.index(")")
            sub_expr = sub_expr[:end]
            while True:
                start = sub_expr.index("(")
                sub_expr = sub_expr[start+1:]
                if "(" not in sub_expr:
                    break

            if sub_expr.isdigit():
                expression = expression.replace("(" + sub_expr + ")", sub_expr)

        if expression.isdigit():
            result += int(expression)
            break
    return result


result = 0
for expression in input_data:
    result += evaluate_expression(expression)

print("final result is", result)
