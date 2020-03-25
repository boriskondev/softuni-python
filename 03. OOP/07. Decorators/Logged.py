def logged(function):
    def wrapper(*args):
        name = f"you called {function.__name__}{args}\n"
        result = f"it returned {function(*args)}"
        return name + str(result)
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

