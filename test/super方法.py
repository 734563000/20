class Foo:
    def f1(self):
        print('foo.f1')
        super().f2()

class Bar:
    def f2(self):
        print('bar.f2')
class sub(Foo,Bar):
    pass

s=sub()


s.f1()