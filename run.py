#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/21 21:45 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

from commen import method  # 从Python包里导入
from testdata import data
from selenium import webdriver # 从selenium工具包里导入webdriver库
driver = webdriver.Chrome()   # webdriver 与chrome建立会话  ==赋值变量
driver.implicitly_wait(10)  # 隐式等待 --设置10s

# 取数据--字典取值
url = data.data_t.get("url")
name = data.data_t["name"]
passwd = data.data_t["passwd"]
key = data.data_t["key"]
print(url,name,passwd,key)

result = method.search_fun(driver=driver,url=url,name=name,passwd=passwd,key=key)  # 调用函数，取值
if key in result:
    print("搜索成功！")
