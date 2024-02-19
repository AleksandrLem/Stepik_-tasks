def greet(name, *args):
    k = ' and '.join(args)
    if len(k) > 0:
        return f'Hello, {name} and {k}!'
    return f'Hello, {name}!'


print(greet('Timur'))
print(greet('Timur', 'Roman'))
print(greet('Timur', 'Roman', 'Ruslan'))
