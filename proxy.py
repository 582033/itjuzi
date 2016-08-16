#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, re
import requests

class proxy():
    def __init__(self):
        pass
        self.url = "http://www.xicidaili.com/nt/"
        self.headers = {
            'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    def get(self):
        header = {}
        html = requests.get(self.url, headers=self.headers).text
        h = re.findall(r'<td>(\d+\.\d+\.\d+\.\d+)</td>\s+<td>(\d+)</td>', html)
        proxy = []
        if len(h) > 0:
            for i in h:
                ip_port = ( "%s:%s" % i).encode('utf-8')
                proxy.append(ip_port)
        return proxy

if __name__ == '__main__':
    proxy = proxy()
    l = proxy.get()
    print l

