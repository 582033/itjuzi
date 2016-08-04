#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib, time
from analysis import isolated
from threading import Thread

def get_data(start, limit):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='itjuzi', charset='utf8')
    cursor = conn.cursor()
    sql = "select juzi_id from faild limit %s,%s" % (start, limit)
    cursor.execute(sql)
    faild_list = []
    for i in cursor.fetchall():
        for juzi_id in i:
            faild_list.append(juzi_id)
    conn.close()
    return faild_list

#多线程补遗
if __name__ == '__main__':
    thread_count = 10
    start = 0
    end = 3000
    workload = (end - start) / thread_count
    for i in range(1, thread_count):
        t_start = start + workload * i
        t_end = start + workload * (i+1) - 1
        flist = get_data(t_start, t_end)

        url = 'http://www.itjuzi.com/company/'
        for id in flist:
            isolated(url, id)
            time.sleep(1)
