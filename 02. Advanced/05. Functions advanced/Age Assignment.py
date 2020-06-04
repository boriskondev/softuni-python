def age_assignment(*args, **kwargs):
    for name in args:
        if name[0] in kwargs:
            kwargs[name] = kwargs[name[0]]
            del kwargs[name[0]]
    return kwargs


print(age_assignment("Peter", "George", G=26, P=19))