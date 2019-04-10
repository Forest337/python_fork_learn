import sys
import os
import time


def save_file():
    fout = open("/Users/zh/Lwh/test1.txt", "w")  #文件保存地址根据自己路径更改

    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    for i in range(5):
        line = str(i) + '写入文件' + now_time + "\n"
        fout.write(line)

    fout.close()


if __name__ == "__main__":

    pid = os.fork()

    print(pid)
    if pid > 0:
        print('我是父进程我被执行了')
        # exit first parent
        print(str('当前脚本进程') + str(os.getppid()))
        print(str('创造出来的父进程') + str(os.getpid()))
        sys.exit(0)
    time.sleep(1)
    print('我是子进程我被执行了')
    os.chdir("/")
    ppid = os.getppid()
    pid = os.getpid()

    # 打印父进程id
    print(ppid)
    # 打印子进程id
    print(pid)
    os.setsid()

    os.umask(0)
    time.sleep(10)

    while True:
        save_file()
        time.sleep(10)


