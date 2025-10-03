import operator

OPERATORS = ('+', '-', '/', '*', '~', '$')
REGEX = r'\d+(\.\d+)?'
PRIORITY = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '~': 3
}
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
