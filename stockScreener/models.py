from django.db import models
# Create your models here.
import sys
import requests
import re



class stock(models.Model):
    stockCode = models.CharField(max_length=10, primary_key=True)
    now = models.IntegerField(null=True, blank=True)
    #diff = models.IntegerField(null=True, blank=True)
    #rate = models.FloatField(null=True, blank=True)
    #high = models.IntegerField(null=True, blank=True)
    #low = models.IntegerField(null=True, blank=True)
    #quant = models.IntegerField(null=True, blank=True)
    #marketSum = models.IntegerField(null=True, blank=True)
    recommendNum = models.IntegerField(null=True, blank=True)

    def checkNow(self):
        print("checkNow")
        print(self.stockCode)
        url = "http://api.finance.naver.com/service/itemSummary.nhn?itemcode="+self.stockCode
        getData = requests.get(url)
        replaceData = getData.text[1:-1].replace('"','').split(',')
        temp = replaceData[11].split(':')
        self.now = temp[1]
        print(self.now)
        self.save()
        return self.now

    def checkRecommendNum(self):
        return self.recommendNum

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
