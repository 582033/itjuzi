#!/usr/bin/env python
# -*- coding:utf8 -*-
import requests, json, re, sys, MySQLdb, cookielib
import random, pprint
from bs4 import BeautifulSoup


def isolated(url, cid):     #从html主体中分离出用户信息{{{
    url = url + str(cid)
    print 'url:' + url
    html_contents = get_soup(url)
    #print html_contents
    #sys.exit()
    if html_contents == None:
        print '----没有获取到内容,更换下一个url'
        print '==================================='
        return None

    print '----开始分析'
    com_name = html_contents.find("input", {"name":"com_name"})['value']                    #获取公司名
    com_sec_name = html_contents.find("input", {"name":"com_sec_name"})['value']            #获取副名
    com_full_name = html_contents.find("input", {"name":"com_registered_name"})['value']    #获取全名
    com_url = html_contents.find("input", {"name":"com_url"})['value']                      #获取网址
    com_desc = html_contents.find("textarea", {"name":"com_des"}).string                    #获取描述

    #获取分类
    category_array = []
    scope = html_contents.find("span", {"class":"scope"}).findAll("a")
    if len(scope) > 0:
        for cat in scope:
            cat_string = charset_utf8(cat.string)
            category_array.append(cat_string)
    company_category = json.dumps(category_array)

    #获取slogan
    com_slogan = ""
    info_line = html_contents.findAll("div", {"class":"info-line"})
    if info_line[0].find("p") != None:
        info_string = info_line[0].find("p").string
        if not re.match(r"Slogan", info_string):
            com_slogan = info_string

    #获取tag
    com_tags = html_contents.find("div", {"class":"tagset"}).findAll("span", {"class":"tag"})
    tags_array = []
    if len(com_tags) > 0:
        for tag in com_tags:
            tag_string = charset_utf8(tag.string)
            tags_array.append(tag_string)
    company_tags = json.dumps(tags_array)

    #获取注册时间
    com_born_year = html_contents.find("select", {"name":"com_born_year"}).findAll('option', selected=True)[0]
    com_born_month = html_contents.find("select", {"name":"com_born_month"}).findAll('option', selected=True)[0]
    com_born = "%s-%s" % (com_born_year.string, com_born_month.string)

    #获取运营状态
    com_status = html_contents.find("select", {"name":"com_status_id"}).findAll('option', selected=True)[0]

    #获取公司规模
    com_scale = html_contents.find("select", {"name":"com_scale"}).findAll('option', selected=True)[0]

    juzi_id = int(cid)                                  #所属IT桔子ID
    company_name = charset_utf8(com_name)               #公司名称
    company_sec_name = charset_utf8(com_sec_name)       #公司副名
    company_full_name = charset_utf8(com_full_name)     #工商注册全称
    company_url = charset_utf8(com_url)                 #公司网址
    company_slogan = charset_utf8(com_slogan)           #公司slogan
    company_description = charset_utf8(com_desc)        #公司描述
    company_born = charset_utf8(com_born)               #注册日期
    company_status = charset_utf8(com_status.string)    #运营状态
    company_scale = charset_utf8(com_scale.string)      #公司规模

    insert_db(juzi_id, company_name, company_sec_name, company_full_name, company_url, company_tags, company_category, company_slogan, company_description, company_born, company_status, company_scale)
#}}}

def get_soup(url):    #返回页面html主体{{{
    headers = {
        'If-Modified-Since' : 'Wed, 03 Aug 2016 03:46:54 GMT',
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    while True:
        ip_address = rand_ip()
        print '--使用代理IP:' + ip_address
        try:
            html = requests.get(url, proxies = {'http':ip_address}, headers=headers, timeout=5)
            #print(html.text)
        except Exception:
            print '--连接异常,更换代理'
            continue
        break
    count = re.findall('<div class="line-title">', html.text)
    print '--打开,url成功,成功匹配到公司名'
    #sys.exit()
    if len(count) < 1:
        print '--没有匹配到公司'
        return None
    soup = BeautifulSoup(html.text)
    soup.prettify()
    return soup
#}}}

def charset_utf8(field):    #{{{
    if field == None:
        new_field = ''
    else:
        sub_field = re.sub(r',\.{3}', '', field)
        new_field = sub_field.encode('utf8').strip()
    return new_field
#}}}

def insert_db(juzi_id, company_name, company_sec_name, company_full_name, company_url, company_tags, company_category, company_slogan, company_description, company_born, company_status, company_scale):  #{{{
    company_obj = {
        'juzi_id' : juzi_id,
        'company_name' : company_name,
        'company_sec_name' : company_sec_name,
        'company_full_name' : company_full_name,
        'company_url' : company_url,
        'company_tags' : company_tags,
        'company_category' : company_category,
        'company_slogan' : company_slogan,
        'company_description' : company_description,
        'company_born' : company_born,
        'company_status' : company_status,
        'company_scale' : company_scale,
    }
    pprint.pprint(company_obj, width=1)
    sys.exit()
    print '----执行插入数据'
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='itjuzi', charset='utf8')
    cursor = conn.cursor()
    sql = "insert into user (juzi_id, company_name, company_sec_name, company_full_name, company_url, company_tags, company_category, company_slogan, company_description, company_born, company_status, company_scale)values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (juzi_id, company_name, company_sec_name, company_full_name, company_url, company_tags, company_category, company_slogan, company_description, company_born, company_status, company_scale))
    conn.commit()
    conn.close()
    print '==============================================='
#}}}

def rand_ip():  #随机获取一个代理IP{{{
    fp = open('proxy.txt', 'r')
    lines = int(len(fp.readlines()))
    num = random.randint(0, lines - 1)
    fp.close()
    fp = open('proxy.txt', 'r')
    ip =  ReadFile(fp, num, 1)
    fp.close()
    return ip
#}}}

def ReadFile(fp, start_line, read_scope):   #读取文件中的某一行{{{
     lines = fp.readlines()
     cursor = 0
     for line in lines:
         line = line.rstrip()
         cursor += 1
         while (cursor > start_line):
             return line
             if (cursor == (start_line+read_scope)):
                 cursor = 0
             break
     fp.close()
#}}}

if __name__ == '__main__':
    isolated('http://www.itjuzi.com/company/', 36079)
