def annon(f):
    def plus():
        print("we first at this to the function")
        f()
        print("we also sdd this at the end")
    return plus

@annon
def Hello():
    print("Hello World")

Hello()