def decor(func):
    def wrap():
        print("=====")
        func()
        print("=====")
    return wrap

@decor
def print_text():
    print("Hello world!")

decorated = print_text
decorated()