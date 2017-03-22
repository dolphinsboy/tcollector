#!/usr/bin/env python
#-*-coding:utf8-*-

import os
import time

################################################
#守护进程的规则
#1.调用umask将文件模式创建屏蔽字设置0
#2.调用fork，然后使父进程退出
#3.调用setsid以创建一个新会话
#4.将当前工作目录更改为根目录
#5.关闭不再需要的文件描述符
#6.将/dev/null使其具有文件描述符0.1和2
################################################

def daemonize():
    #创建子进程
    if os.fork():
        #主进程
        #print os.getpid()
        os._exit(0)
    #子进程
    #print os.getppid()
    os.chdir("/")
    os.umask(022)
    os.setsid()
    os.umask(0)

    if os.fork():
        #当前进程
        os._exit(0)
    #当前进程的子进程
    stdin = open(os.devnull)
    stdout = open(os.devnull, 'w')
    os.dup2(stdin.fileno(), 0)
    os.dup2(stdout.fileno(), 1)
    os.dup2(stdout.fileno(), 2)
    stdin.close()
    stdout.close()
    os.umask(022)

    #关闭所有描述符
    for fd in xrange(3, 1024):
        try:
            os.close(fd)
        except OSError:
            pass
def run():
    while True:
        with open("/Users/guosong/opdir/20170322/test.log", "a") as f:
            f.writelines("A")
            f.writelines(os.path.abspath("./"))
            time.sleep(5)

def main():
    daemonize()
    run()

if __name__ == '__main__':
    main()
