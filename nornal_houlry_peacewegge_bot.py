from django.shortcuts import render
from django.http import HttpResponse
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
from .models import Index , CasPceWagesEntry
from selenium.webdriver.common.alert import Alert
list_range=[]


def Normal_houlry_peace_wedge_bot(request):
    if request.method=="GET":
        return render (request,'index.html')
    else:
        startrange=request.POST.get('startrange1')
        endange=request.POST.get('endrange1')
        # print(startrange,endange)
        list_range.append(startrange)
        list_range.append(" "+"TO"+" ")
        list_range.append(endange)
        # return HttpResponse("done")
        
        sheet_url = "https://docs.google.com/spreadsheets/d/1oFRyFMn1L2-yRnspTMocLBDgZMPLOQeK8Vt68SbEjLA/edit#gid=0"
        url_1 = sheet_url.replace("/edit#gid=", "/export?format=csv&gid=") 
        df=pd.read_csv(url_1)

        # print(type(df))

        driver=webdriver.Chrome(ChromeDriverManager().install())

        # driver=webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

        driver.get('http://faltawageexcel.stockexcel.com/pce_WagesEntry.aspx?PageID=DataEntry')