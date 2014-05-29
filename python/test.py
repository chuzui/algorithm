x = 99
def f1():
    x = 88
    def f2():
        nonlocal x
        x = 77
        # print(x)
    f2()
    print(x)
f1()