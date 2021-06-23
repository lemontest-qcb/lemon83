#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/6/21 21:44 
# @Author : Lemon_Tricy
# @QQ: 2378807189
# Copyright：湖南省零檬信息技术有限公司

import time
# 打开网页
def open_page(driver,url):
    driver.get(url)
    driver.maximize_window()
# 登录函数
def login_fun(driver,name,passwd):
    driver.find_element_by_name("username").send_keys(name)
    driver.find_element_by_name("password").send_keys(passwd)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()

# 搜索函数
def search_fun(driver,url,name,passwd,key):
    open_page(driver,url)
    login_fun(driver,name,passwd)
    driver.find_element_by_xpath("//div[@id='leftMenu']//span[text()='零售出库']").click()
    id = driver.find_element_by_xpath('//div[text()="零售出库"]/..').get_attribute("id")   # 获取id属性
    id_iframe = id + "-frame"   # 通过字符出阿奴的拼接 得到iframe id
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    driver.find_element_by_id("searchNumber").send_keys(key)
    driver.find_element_by_id("searchBtn").click()  # 点击查询按钮
    time.sleep(1)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num

