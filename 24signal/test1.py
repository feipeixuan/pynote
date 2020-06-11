#coding:utf-8

import signal

def handle_hup(sig, frame):
    print ("get signal: %s"%sig)

signal.signal(1, handle_hup)
#获取 signal 中定义的信号 num 和名称，还有它的 handler 是什么
if __name__ == "__main__":

    ign = signal.SIG_IGN
    dfl = signal.SIG_DFL
    # signal.SIG_IGN（表示被忽略）, signal.SIG_DFL（默认行为已经被使用）或
    # None（Python的handler还没被定义）
    print ("SIG_IGN", ign)
    print ("SIG_DFL", dfl)
    print ("*"*40)

    for name in dir(signal):
        if name[:3] == "SIG" and name[3] != "_":
            signum = getattr(signal, name)
            gsig = signal.getsignal(signum)  #Return the current signal handler for the signal signalnum

            print (name, signum, gsig)

####总结
# 1.大部分信号都是都有默认的行为
# 2.常用的几个信号：

# 1.SIGHUP终端挂起或者终止进程。默认动作为终止进程
# 2.SIGINT键盘中断<ctrl+c>经常会用到。默认动作为终止进程
# 3.SIGQUIT键盘退出键被按下。一般用来响应<ctrl+d>。 默认动作终止进程
# 9.SIGKILL强制退出。 shell中经常使用
# 14.SIGALRM定时器超时，默认为终止进程
# 15.SIGTERM程序结束信号，程序一般会清理完状态在退出，我们一般说的优雅的退出