#!/usr/bin/env python
# -*- coding: utf-8 -*-
from proxy import proxy

print "======================"
print "== 开始获取代理列表 =="
print "======================"

def get_proxies():
    proxy_url = "http://www.xicidaili.com/nt/"      #代理来源
    target_url = "http://www.itjuzi.com/company/1"  #验证代理的url
    ver_keyword = "com_id"                          #验证关键字
    timeout = 10                                    #验证超时时间

    proxy = proxy(proxy_url, target_url, ver_keyword, timeout)
    proxies = proxy.get()
    return proxies

print get_proxies

print "======================"
print "== 加载代理列表完成 =="
print "======================"
