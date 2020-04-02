
class Base1:


    def __init__(self,a,b):
        self.a=a
        self.b=b


    def run(self):
        print("base1")


class Base2:


    def __init__(self,c):
        super(Base2,self).__init__()

    def run(self):
        print("base2")

class child1(Base1,Base2):

    def __init__(self):
        pass

    def run(self):
        Base1.run(self)
        Base2.run(self)
        print("child1")



c1=child1()
c1.run()
