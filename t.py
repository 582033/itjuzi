#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib, time

if __name__ == '__main__':
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='itjuzi', charset='utf8')
    cursor = conn.cursor()
    sql = "delete from faild where juzi_id='16'"
    cursor.execute(sql)
    conn.commit()
    conn.close()
