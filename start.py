#!/usr/bin/env python
# -*- coding:utf8 -*-
import time
from analysis import isolated


if __name__ == '__main__':
    url = 'http://www.itjuzi.com/company/'
    for i in range(74, 500):
        isolated(url, i)
        time.sleep(3)
