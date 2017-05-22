from django.db import models
# Create your models here.
import sys
import requests
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


class stock(models.Model):
    stockCode = models.CharField(max_length=10, primary_key=True)
    now = models.IntegerField(null=True, blank=True)
    ma5 = models.IntegerField(null=True, blank=True)
    ma20 = models.IntegerField(null=True, blank=True)
    ma60 = models.IntegerField(null=True, blank=True)
    #diff = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    #high = models.IntegerField(null=True, blank=True)
    #low = models.IntegerField(null=True, blank=True)
    #quant = models.IntegerField(null=True, blank=True)
    #marketSum = models.IntegerField(null=True, blank=True)
    #recommendNum = models.IntegerField(null=True, blank=True)

    def checkStockNow(self):
        print("checkNow")
        print(self.stockCode)
        url = "http://api.finance.naver.com/service/itemSummary.nhn?itemcode="+self.stockCode
        getData = requests.get(url)
        replaceData = getData.text[1:-1].replace('"','').split(',')
        tempNow = replaceData[11].split(':')
        tempRate = replaceData[3].split(':')
        self.now = tempNow[1]
        self.rate = tempRate[1]
        print(self.now)
        print(self.rate)
        self.save()

    def checkStockMA(self):
        url = 'http://finance.daum.net/item/quote_avg_yyyymmdd_sub2.daum?code=' + self.stockCode
        html = urlopen(url)
        source = BeautifulSoup(html.read(), "html.parser")
        srlists=source.find_all("tr")
        isCheckNone = None

        if(srlists[2].span != isCheckNone):
            #print(srlists[2])
            #print(srlists[2].find_all("td",class_="datetime2")[0].text) #날짜
            print(srlists[2].find_all("td",class_="num")[3].text) #5일선
            self.ma5 = int(srlists[2].find_all("td",class_="num")[3].text.strip().replace(",",""))
            #print(srlists[2].find_all("td",class_="num")[4].text) #10일선
            print(srlists[2].find_all("td",class_="num")[5].text) #20일선
            self.ma20 = int(srlists[2].find_all("td",class_="num")[5].text.strip().replace(",",""))
            print(srlists[2].find_all("td",class_="num")[6].text) #60일선
            self.ma60 = int(srlists[2].find_all("td",class_="num")[6].text.strip().replace(",",""))
            #print(srlists[2].find_all("td",class_="num")[7].text) #120일선
        self.save()

    def checkRecommendNum(self):
        return self.recommendNum

    def showStockInfo(self):
        return dict(
            stockCode=self.stockCode,
            now = self.now,
            rate = self.rate,
            ma5 = self.ma5,
            ma20 = self.ma20,
            ma60 = self.ma60,)

#import sys
#import requests
#import re
#import time

#start_time = time.time()

#for i in range(0,1):
#   code = "053800"
#    url = "http://api.finance.naver.com/service/itemSummary.nhn?itemcode="+code
#    s = requests.get(url)
#    print (s.text)
#plain_text = s.text[1:-1].replace('"','').split(',')
#print (plain_text)

#end_time = time.time()


#print (end_time - start_time)

#soup = BeautifulSoup(plain_text, "lxml")
#ranks = soup.find("marketSum")

#print (ranks.get_text())
