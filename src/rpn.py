import re
from src.constants import OPERATORS, REGEX, PRIORITY
from src.calculatorerror import CalcError

def rpn(tokens: list[str]) -> list[str]:
    out: list[str] = []
    stack: list[str] = []

    for token in tokens:
        if re.match(REGEX, token):
            out.append(token)
        elif token in OPERATORS:
            while stack and stack[-1] in OPERATORS and PRIORITY[stack[-1]] >= PRIORITY[token]:
                out.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            if not stack:
                raise CalcError('Ошибка ввода скобок')
            stack.pop()
        else:
            raise CalcError(f'Неправильный ввод: {token}')

    while stack:
        op = stack.pop()
        if op in '()':
            raise CalcError('Ошибка ввода скобок')
        out.append(op)

    return out
