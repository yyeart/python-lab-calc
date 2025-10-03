import re
from src.constants import OPERATORS, REGEX, OPERATIONS
from src.calculatorerror import CalcError

def calculate(rpn_tokens: list[str]) -> int | float:
    stack = []
    for token in rpn_tokens:
        if re.match(REGEX, token):
            stack.append(float(token))
        elif token in OPERATORS:
            if token == '~':
                a = stack.pop()
                stack.append(-a)
            else:
                b, a = stack.pop(), stack.pop()
                if token == '/' and b == 0:
                    raise CalcError('Деление на ноль')
                stack.append(OPERATIONS[token](a, b))
        else:
            raise CalcError(f'Неизвестный символ: {token}')

    if len(stack) != 1:
        raise CalcError('Ошибка вычисления')

    result = stack[0]
    return int(result) if result.is_integer() else result
