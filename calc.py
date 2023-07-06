
expression = input("Введите выражение: ")

compiled = compile(expression, 'string', 'eval')

print(eval(compiled))

