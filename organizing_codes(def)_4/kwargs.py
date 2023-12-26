def do_calculation(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)


do_calculation('Jeff', 4, 6, 3, 7, a=1, b=2, c=3)

# example


def concatenate(**words):
    sentence = ''
    for word in words.values():
        sentence += word + ' '
    print(sentence)


concatenate(a='We', b='Are', c='Pythonistas', d='Professionals')
