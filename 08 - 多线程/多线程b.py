#!/usr/bin/env python
#-*- coding:utf-8 -*-

import thread
from time import sleep, ctime

loops = [4, 2]# 第一次延时4秒  第二次延时两秒

# 定义loop函数 为创建多线程 做准备
def loop (nloop, nsec, lock): # 参一: 执行线程名字  参二：延时/s  参三：传递"锁"的对象
    # 执行前输出信息  ctime记录当前时间
    print 'start loop', nloop, 'at:', ctime()
    # 延时多少秒后执行下面
    sleep( nsec )
    # 本条线程执行完成 输出文字
    print 'loop', nloop, 'done at:', ctime() 
    # 释放锁  传进来的锁，让他解锁
    lock.release() 

# 主函数
def main():
    # 输出执行主函数时间
    print 'starting at:', ctime()
    # 定义一个空列表 用来装锁对象
    locks = []
    # 生成0,1的列表 用来迭代
    nloops = range(len(loops))

    # 迭代0 1  生成两个锁对象
    for i in nloops:
        # 分配两个锁对象
        lock = thread.allocate_lock()
        # 给锁对象加上锁  执行加锁方法
        lock.acquire()
        # 把加好锁的对象放进列表 一同传参
        locks.append(lock)
        
    for i in nloops:# 创建两条子线程相互不影响
        # 创建子线程 把锁对象和延时多少秒传进去
        thread.start_new_thread( loop, (i, loops[i], locks[i]) )

    # 执行死循环 当锁列表里的两个锁对象都被释放(解锁) 的时候跳出循环
    # 为了等待子线程执行 锁释放(解锁)lock.release()  然后再执行主线程
    for i in nloops:
        while locks[i].locked():pass
    # 锁都被释放完 主线程执行到这 打印输出 执行完成
    print 'all Dat:', ctime()

# 主函数入口
if __name__ == '__main__':
    main()
