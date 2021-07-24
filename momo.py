#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
#另外創setting.py 檔案內宣告變數pwd為密碼 mo1為欲購買物品網址
import setting
import importlib

importlib.reload(setting)


driver_path = '[chromedriver.exe路徑]'
options = webdriver.ChromeOptions()
#開啟chrome前往chrome://version/ 複製設定檔路徑取代以下中括號
options.add_argument(r"--user-data-dir=[chrome設定檔路徑]")
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(setting.mo1)

#加入購物車
while 1:
    try:
        WebDriverWait(driver, 3, 0.3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="buy_yes"]/a/img'))
        )  
        driver.find_element_by_xpath('//*[@id="buy_yes"]/a/img').click()
        print('有貨')
        break;
    except:
        driver.refresh()
        print('未開賣')

#帳號
acc = WebDriverWait(driver, 30).until(
    expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="memId"]'))
)
acc.click()

#密碼
pwd_show = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="passwd_show"]'))
)
pwd_show.click()
pwd = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="passwd"]'))
)
pwd.send_keys(setting.pwd)

#登入
login = WebDriverWait(driver, 10).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/dl[2]/dd[7]/input'))
)  
driver.find_element_by_xpath('//*[@id="loginForm"]/dl[2]/dd[7]/input').click()

#結帳
WebDriverWait(driver, 30).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="shpSumm"]/div/ul/li[1]/a'))
)  
driver.find_element_by_xpath('//*[@id="shpSumm"]/div/ul/li[1]/a').click()

#選取Line Pay
WebDriverWait(driver, 30).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="linepay15"]'))
)  
driver.find_element_by_xpath('//*[@id="linepay15"]').click()

#確認送出
WebDriverWait(driver, 30).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="orderSave"]'))
)  
driver.find_element_by_xpath('//*[@id="orderSave"]').click()
