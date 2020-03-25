# class decorator_class(object):
#     def __init__(self, original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print(f"Call method executed this before {self.original_function.__name__}")
#         return self.original_function(*args, **kwargs)


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("Display function ran.")


display()