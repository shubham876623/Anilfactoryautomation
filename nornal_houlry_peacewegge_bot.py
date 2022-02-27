# from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.
import requests
import pandas as pd
from io import BytesIO

from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from random import seed
from random import random
from time import process_time, sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import csv
from urllib.request import urlopen
from selenium.webdriver.support.select import Select
# from .models import Index , CasPceWagesEntry
from selenium.webdriver.common.alert import Alert
list_range=[]


# def Normal_houlry_peace_wedge(request):

    # if request.method=="GET":
    #     return render (request,'index.html')
    # else:

    # startrange=request.POST.get('startrange1')
    # endange=request.POST.get('endrange1')
    # print(startrange,endange)
    # list_range.append(startrange)
    # list_range.append(" "+"TO"+" ")
    # list_range.append(endange)
    # return HttpResponse("done")
    
sheet_url = "https://docs.google.com/spreadsheets/d/1e8IZNa36vrLSPXkOL7xrgd2EYV2vJOJWHtAGW_drGhQ/edit#gid=0"
url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=") 
df=pd.read_csv(url_1)
# print(df)
# print(type(df))

driver=webdriver.Chrome(ChromeDriverManager().install())

# driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

driver.get('http://faltawageexcel.stockexcel.com/HourlyWageEntry.aspx?PageID=DataEntry')
driver.maximize_window()

time.sleep(3)
driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/input').send_keys('shubham')
driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys('suv@123')
driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys(Keys.ENTER)
# for _ in range(3):
time.sleep(5)
actions = ActionChains(driver)
alert = Alert(driver)


# accept the alert
alert.accept()

driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys('suv@123')
driver.find_element_by_xpath('/html/body/form/div[3]/div[5]/input').send_keys(Keys.ENTER)
for i in range(3,len(df['Worker No'].values.tolist())+1):

    driver.get('http://faltawageexcel.stockexcel.com/HourlyWageEntry.aspx?PageID=DataEntry')
    # enter worker number ..abs(x)
    driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div[1]/div/table/tbody/tr[7]/td[1]/table/tbody/tr[1]/td[1]/input').send_keys(str(df['Worker No'][i]))
    # time.sleep(3)
    # select buyer code ..
    
    driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div[1]/div/table/tbody/tr[7]/td[2]/table/tbody/tr/td[1]/select').send_keys(str(df['Buyer Code'][i]))
    # select order number ..abs
    time.sleep(5)
    # driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo').send_keys(str(df['Buyer Code'][i]))
     # slecting order number code  .....
    while True :
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
        if el is not None:
           
    
     
            if int(float(df['Order No'][i]))<10:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(("00")+str(int(float(df['Order No'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break
            elif 10<int(float(df['Order No'][i]))<100:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(("0")+str(int(float(df['Order No'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break        
            else:
                el = driver.find_element_by_id('ContentPlaceHolder1_ddlOrderNo')
                # el = driver.find_element_by_id('id_of_select')
                for option in el.find_elements_by_tag_name('option'):
                    if option.text == '{}'.format(str(int(float(df['Order No'][i])))):
                        option.click() # select() in earlier versions of webdriver
                        break        
            break            
    # slect in time ..
    
    if int(float(df['Hourin'][i]))<10:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlInHour')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("0")+str(int(float(df['Hourin'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
     
    else:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlInHour')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(int(float(df['Hourin'][i])))):
                option.click() # select() in earlier versions of webdriver
                break 
            
            
    ###  ..    selecting minutes 
    
        
    if int(float(df['Minutesin'][i]))<10:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlInMinute')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("0")+str(int(float(df['Minutesin'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
     
    else:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlInMinute')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(int(float(df['Minutesin'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
            
            
    ##### ........   slecting outtime......
      ###........ for hourout.......
    
    if int(float(df['Hourout'][i]))<10:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlOutHour')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("0")+str(int(float(df['Hourout'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
     
    else:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlOutHour')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(int(float(df['Hourout'][i])))):
                option.click() # select() in earlier versions of webdriver
                break  
    
    ##...........for minutesout.......
    if int(float(df['Minutesout'][i]))<10:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlOutMinute')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(("0")+str(int(float(df['Minutesout'][i])))):
                option.click() # select() in earlier versions of webdriver
                break
     
    else:
        el = driver.find_element_by_id('ContentPlaceHolder1_ddlOutMinute')
        # el = driver.find_element_by_id('id_of_select')
        for option in el.find_elements_by_tag_name('option'):
            if option.text == '{}'.format(str(int(float(df['Minutesout'][i])))):
                option.click() # select() in earlier versions of webdriver
                break  
            
            
        ##..... slecting date.......
        
        # driver.find_element_by_id('ContentPlaceHolder1_txtDate').clear()
        # driver.find_element_by_id('ContentPlaceHolder1_txtDate').send_keys(str(df['Date'][i]))
    driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div[1]/div/table/tbody/tr[7]/td[6]/table/tbody/tr/td[1]/input').clear()
    driver.find_element_by_xpath('/html/body/form/div[3]/div[3]/div[3]/div/div[1]/div/table/tbody/tr[7]/td[6]/table/tbody/tr/td[1]/input').send_keys(str(df['Date'][i]))
    # clicking on submit ..
    driver.find_element_by_id('ContentPlaceHolder1_btnSubmit').click()
    time.sleep(2)