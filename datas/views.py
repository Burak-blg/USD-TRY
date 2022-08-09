from urllib import request

from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

#from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True


# Create your views here.
def index(request):
    if request.method == "POST":

         browser2 = webdriver.Chrome(options=options)
         url2 = "https://www.exchangerates.org.uk/USD-TRY-exchange-rate-history.html"
         browser2.get(url2)

         dollar = browser2.find_elements(By.CSS_SELECTOR, "tr[class='colone']")
         dollar2 = browser2.find_elements(By.CSS_SELECTOR, "tr[class='coltwo']")


         def convert(lst):
              return (lst.split())

         datas = []
         labels = []

         for x in range(len(dollar)):
              datas.append(float(convert(dollar[x].text)[7]))

              datas.append(float(convert(dollar2[x].text)[7]))

         for x in range(len(dollar)):
              labels.append(convert(dollar[x].text)[13])

              labels.append(convert(dollar2[x].text)[13])

         browser2.close()
         labels.reverse()
         datas.reverse()

         return render(request,'index.html',{'datas':datas,'labels':labels})

    return render(request,'index.html')