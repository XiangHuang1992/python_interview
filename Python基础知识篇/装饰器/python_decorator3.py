import logging

def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__)
        print(func.__doc__)
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
    """ do something  """
    return x + x * x

logged(f)
