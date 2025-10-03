import re
from src.calculatorerror import CalcError
from src.constants import REGEX

def tokenize(expression: str) -> list[str]:
    tokens = list()
    expression = expression.replace(' ', '')
    pattern = re.compile(fr'{REGEX}|[+\-*/()]')
    index = 0
    while index < len(expression):
        matches = pattern.match(expression, index)
        if not matches:
            raise CalcError(f'Неправильный ввод: "{expression[index]}"')
        tokens.append(matches.group())
        index = matches.end()
    return tokens
