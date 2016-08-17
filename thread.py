#!/usr/bin/env python
# -*- coding:utf8 -*-

import time, sys
from proxy import Proxy
import threading
import analysis as ass

def get_proxies():
    proxy_url = "http://www.xicidaili.com/nt/"      #代理来源
    target_url = "http://www.itjuzi.com/company/1"  #验证代理的url
    ver_keyword = "com_id"                          #验证关键字
    timeout = 10                                    #验证超时时间

    p = Proxy(proxy_url, target_url, ver_keyword, timeout)
    proxies = p.get()
    return proxies


def loop(start, end):
    url = 'http://www.itjuzi.com/company/'
    for i in range(start, end):
        ass.isolated(url, i)
        time.sleep(0.5)

if __name__ == '__main__':
    print "======================"
    print "== 开始获取代理列表 =="
    print "======================"

    proxies = get_proxies()

    print "======================"
    print "== 加载代理列表完成 =="
    print "======================"
    ass.set_global(proxies)

    thread_count = 10
    start = 0
    end = 43000
    workload = (end - start) / thread_count
    for i in range(1, thread_count):
        t_start = start + workload * i
        t_end = start + workload * (i+1) - 1
        threading.Thread(target=loop, args=(t_start, t_end)).start()
    sys.exit()
