


def fn(self, name='world'):  # 假如我们有一个函数叫fn
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(say_hello=fn,name="22"))
#动态创建类type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)

hello  =  Hello()
hello.say_hello()
print(hello.name)

#metaclass允许你创建类或者修改类。换句话说，你可以把类看成是元类创建出来的“实例”
