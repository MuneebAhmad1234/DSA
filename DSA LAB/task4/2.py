def evaluate_postfix(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)
    return stack.pop()

expressions = [
    "5 1 2 + 4 * + 3 -",
    "2 3 + 5 *",
    "10 2 8 * + 3 /",
    "3 4 + 2 * 7 /",
]

for expr in expressions:
    print(f"Expression: {expr} => Result: {evaluate_postfix(expr)}")
