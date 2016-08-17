#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib, time
import threading
import Queue
import analysis as ass
from proxy import Proxy

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

def get_proxies():
    proxy_url = "http://www.xicidaili.com/nt/"      #代理来源
    target_url = "http://www.itjuzi.com/company/1"  #验证代理的url
    ver_keyword = "com_id"                          #验证关键字
    timeout = 10                                    #验证超时时间

    p = Proxy(proxy_url, target_url, ver_keyword, timeout)
    proxies = p.get()
    return proxies

def loop(flist):
    url = 'http://www.itjuzi.com/company/'
    for i in flist:
        ass.isolated(url, i)
        time.sleep(0.5)

#多线程补遗
if __name__ == '__main__':
    print "======================"
    print "== 开始获取代理列表 =="
    print "======================"

    proxies = get_proxies()

    print "======================"
    print "== 加载代理列表完成 =="
    print "======================"
    ass.set_global(proxies)

    thread_count = 20
    start = 0
    end = 8200
    workload = (end - start) / thread_count
    queue = Queue.Queue()
    for i in range(1, thread_count):
        t_start = start + workload * i
        t_end = start + workload * (i+1) - 1
        threading.Thread(target=get_data, args=(t_start, t_end, queue)).start()
        threading.Thread(target=loop, args=(queue.get(), )).start()

    sys.exit()
