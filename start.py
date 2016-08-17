#!/usr/bin/env python
# -*- coding:utf8 -*-

import time, sys
from proxy import Proxy
import analysis as ass

def get_proxies():
    proxy_url = "http://www.xicidaili.com/nt/"      #代理来源
    target_url = "http://www.itjuzi.com/company/1"  #验证代理的url
    ver_keyword = "com_id"                          #验证关键字
    timeout = 10                                    #验证超时时间

    p = Proxy(proxy_url, target_url, ver_keyword, timeout)
    proxies = p.get()
    return proxies

if __name__ == '__main__':
    print "======================"
    print "== 开始获取代理列表 =="
    print "======================"

    proxies = get_proxies()

    print "======================"
    print "== 加载代理列表完成 =="
    print "======================"

    ass.set_global(proxies)

    url = 'http://www.itjuzi.com/company/'
    start = int(sys.argv[1])
    end = int(sys.argv[2])+1
    for i in range(start, end):
        ass.isolated(url, i)
        time.sleep(1)
    sys.exit()
