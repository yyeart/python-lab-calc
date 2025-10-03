from src.tokenize import tokenize
from src.rpn import rpn
from src.calculate import calculate

def main() -> None:
    try:
        expression = input()
        tokens = tokenize(expression)
        rpn_tokens = rpn(tokens)
        result = calculate(rpn_tokens)

        print(result)
    except Exception as e:
        print(f'Ошибка: {e}')

if __name__ == '__main__':
    main()
