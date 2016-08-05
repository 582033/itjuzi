#!/usr/bin/env python
# -*- coding:utf8 -*-
import time, sys
from analysis import isolated
from Queue import Queue
from threading import Thread

if __name__ == '__main__':
    url = 'http://www.itjuzi.com/company/'
    start = int(sys.argv[1])
    end = int(sys.argv[2])+1
    for i in range(start, end):
        isolated(url, i)
        time.sleep(1)
    sys.exit()
