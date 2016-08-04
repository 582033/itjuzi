#!/usr/bin/env python
# -*- coding:utf8 -*-
import time, sys
from analysis import isolated
from threading import Thread


def loop(start, end):
    url = 'http://www.itjuzi.com/company/'
    for i in range(start, end):
        isolated(url, i)
        time.sleep(1)

if __name__ == '__main__':
    thread_count = 10
    start = 10000
    end = 20000
    workload = (end - start) / thread_count
    for i in range(1, thread_count):
        t_start = start + workload * i
        t_end = start + workload * (i+1) - 1
        Thread(target=loop, args=(t_start, t_end, )).start()
    sys.exit()
