# def function

def annouce(f):
    def wrapper():
        print("about to run the function..")
        f()
        print("done with the function")
    return wrapper



@annouce # hello function wrapped in this announce, sort like nested
def hello():
    print("hello, world")


hello()