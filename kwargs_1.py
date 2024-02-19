def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(f'{key}: {value}')

    # print(sorted(kwargs))


info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')
