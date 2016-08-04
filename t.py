#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib


def escape():
    foo = [u'\u56e2\u8d2d', u'\u5973\u6027\u7ecf\u6d4e', u'\u793e\u4f1a\u5316\u7535\u5546', u'\u5bfc\u8d2d', u'IBM\u7cfb', u'\u7535\u5b50\u5546\u52a1', u'\u7efc\u5408\u7535\u5546', u'\u7535\u5546\u5a92\u4f53\u53ca\u793e\u533a', u'\u5176\u4ed6\u7535\u5546\u670d\u52a1']
    #for bar in foo:
        #print bar

    print json.dumps(foo, ensure_ascii=False)

def get_data(juzi_id):
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='itjuzi', charset='utf8')
    cursor = conn.cursor()
    sql = "select * from company where juzi_id = %s"
    cursor.execute(sql, [juzi_id])
    for data in cursor.fetchone():
        print data


if __name__ == '__main__':
    #get_data(1)
    #escape()
    #print foo.decode('utf-8')
    foo = range(1, 10+1)
    for i in foo:
        print i
