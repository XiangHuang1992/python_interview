class Foo():
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print("class decorator is running")
        self._func()
        print("class decorator ending")


@Foo
def bar():
    print("bar")



bar()
