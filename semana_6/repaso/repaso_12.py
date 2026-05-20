
x = 5

def outer():
    x = 10
    def inner():
        print(x)
    inner()


outer()
print(x)
