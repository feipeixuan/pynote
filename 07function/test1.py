
class A:

    def a(self,content):
        print("a"+content)

    def b(self, content):
        print("b" + content)

    def sum(self, content):
        funcs = [self.a,self.b]
        for func in funcs:
            func(content)


    # def sum(self, content):
    #     funcs = [A.a, A.b]
    #     for func in funcs:
    #         func(self, content)


a=A()
a.sum("2222")