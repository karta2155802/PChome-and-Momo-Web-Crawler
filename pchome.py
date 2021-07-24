#!/usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time
#另外創setting.py 檔案內宣告變數pwd為密碼 pc1為欲購買物品網址
import setting
import importlib

importlib.reload(setting)


driver_path = '[chromedriver.exe路徑]'
options = webdriver.ChromeOptions()
#開啟chrome前往chrome://version/ 複製設定檔路徑取代以下中括號
options.add_argument(r"--user-data-dir=[chrome設定檔路徑]")
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get(setting.pc1)

#加入購物車
while 1:
    try:
        WebDriverWait(driver,30, 0.3).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="ButtonContainer"]/button'))
        )  
        driver.find_element_by_xpath('//*[@id="ButtonContainer"]/button').click()
        
        #處理沒貨彈出視窗
        alert = driver.switch_to.alert
        alert.accept()
        driver.refresh()
        time.sleep(0.8)
        print('未開賣')
    except:
        print('有貨')
        break;
        
time.sleep(0.05)

#進入購物車
WebDriverWait(driver,30).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="ServiceContainer"]/li[1]/a'))
)  
driver.find_element_by_xpath('//*[@id="ServiceContainer"]/li[1]/a').click()

#選取Line Pay
WebDriverWait(driver,20).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="payment_tappay"]/dd/ul/li[1]/a[1]'))
)  
driver.find_element_by_xpath('//*[@id="payment_tappay"]/dd/ul/li[1]/a[1]').click()

#確認送出
WebDriverWait(driver,20).until(
    expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="btnSubmit"]'))
)  
driver.find_element_by_xpath('//*[@id="btnSubmit"]').click()
