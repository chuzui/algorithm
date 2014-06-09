class A:
    count = 0
    def __init__(self):
        self.count += 1

a = A()
print(a.count)
b = A()
print(a.count)
print(b.count)