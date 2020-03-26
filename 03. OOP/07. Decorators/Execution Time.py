from datetime import datetime


def exec_time(func):
    def wrapper(*args):
        start = datetime.now()
        func(*args)
        end = datetime.now()
        time_took = end - start
        return time_took.seconds
    return wrapper


@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total


print(loop(1, 10000000))


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))

