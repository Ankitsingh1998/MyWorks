def equal(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def star(func):
    def wrap():
        print("************")
        func()
        print("************")
    return wrap

def slash(func):
    def wrap():
        print("////////////")
        func()
        print("\\\\\\\\\\\\\\\\\\\\\\\\")
    return wrap
def backslash(func):
    def wrap():
        print("\\\\\\\\\\\\\\\\\\\\\\\\")
        func()
        print("////////////")
    return wrap



@equal
@slash
@star
@backslash
def print_text():
    print("Hello world!")

print_text()


print('\n \n')

def new(func):
    def wrap():
        print("************")
        print("////////////")
        func()
        print("\\\\\\\\\\\\\\\\\\\\\\\\")
        print("************")
    return wrap
@new
def print_text():
    print("Hello world!")

print_text()