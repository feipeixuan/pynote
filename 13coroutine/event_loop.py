def fun():
    print("step1")
    yield
    print("step2")
    yield
    print("step3")
    yield


scheduled_list = []


class Handle(object):
    def __init__(self, gen):
        self.gen = gen

    def call(self):
        try:
            next(self.gen)
        except Exception as e:
            pass
        else:
            scheduled_list.append(self)


def loop(*coroutines):
    scheduled_list.extend(Handle(c) for c in coroutines)
    while True:
        while scheduled_list:
            handle = scheduled_list.pop(0)
            handle.call()
            # if len(scheduled_list)==0:
            #     exit()


if __name__ == "__main__":
    loop(fun(), fun(), fun())

# 将生成器的每一步都当成是一次调用，把生成器包装成一个Handle对象，每次调用handle对象的call来完成生成器的调用，
# 同时，我们还可以在调用完成后做一些准备来控制下一次调用的时间，将Handle对应放到一个scheduled_list里面