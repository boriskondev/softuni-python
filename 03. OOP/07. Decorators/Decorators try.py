def multiply_string(times):
    def decorator(func):
        def wrapper(*args):
            func_result = func(*args)
            result = ""
            result += f"{func_result}\n" * times
            return result
        return wrapper
    return decorator


def to_upper(func):
    def wrapper(*args):
        result = func(*args).upper()
        return result
    return wrapper


@multiply_string(2)
@to_upper
def get_name(name):
    return "Hello, " + name + "!"


print(get_name(input("What is your name? ")))