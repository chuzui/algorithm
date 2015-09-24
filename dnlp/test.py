from multiprocessing import Pool

class A:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

if __name__ == '__main__':
    objs = [A() for i in range(3)]

    p = Pool(3)

    re = p.map(lambda a: a.set_name("asda"), objs)

    p.join()

    pass