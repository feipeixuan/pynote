import time

class TimeTest(object):

    x=3
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @staticmethod
    def showTime():
        print(TimeTest.x)
        return time.strftime("%H:%M:%S", time.localtime())

    @classmethod
    def test(cls):
        print(cls.x)

TimeTest.showTime()


