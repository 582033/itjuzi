#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib, time
from analysis import isolated
from threading import Thread
from Queue import Queue

def get_data(start, limit, queue):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='itjuzi', charset='utf8')
    cursor = conn.cursor()
    sql = "select juzi_id from faild limit %s,%s" % (start, limit)
    cursor.execute(sql)
    faild_list = []
    for i in cursor.fetchall():
        for juzi_id in i:
            faild_list.append(juzi_id)
    conn.close()
    queue.put(faild_list)

def loop(flist):
    url = 'http://www.itjuzi.com/company/'
    for i in flist:
        isolated(url, i)
        time.sleep(1)

#多线程补遗
if __name__ == '__main__':
    thread_count = 10
    start = 3000
    end = 7000
    workload = (end - start) / thread_count
    queue = Queue()
    for i in range(1, thread_count):
        t_start = start + workload * i
        t_end = start + workload * (i+1) - 1
        Thread(target=get_data, args=(t_start, t_end, queue)).start()
        Thread(target=loop, args=(queue.get(), )).start()

    sys.exit()
