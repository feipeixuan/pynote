# coding=utf8

def consumer():
    def test():
        data="22"
        while True:
            data=(yield data)
            print("consumer {0}".format(data))
    return test


def produce(gen):
    gen.__next__()
    def test():
        print(gen.send("333"))
        print(gen.send("444"))
    return test
func=consumer()
gen=func()
p=produce(gen)
p()


