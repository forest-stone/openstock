from django.db import models
from django.utils import timezone
from stockScreener.models import stock

# Create your models here.
class item(models.Model):
    url = models.URLField(primary_key=True)
    title = models.CharField(max_length=20)
    leadingPeriod = models.IntegerField()
    leadingType = models.CharField(max_length=10)
    stockNum = models.IntegerField()
    stockCode = models.CharField(max_length=20)
    stockNow = models.CharField(default=0, max_length=30)
    createDate = models.DateTimeField(default=timezone.now)

    def showitem(self):
        tempCodeList = self.stockCode.split(',')
        tempNowList = self.stockNow.split(',')
        rate = 0;
        print(self.url)
        i = 0
        try:
            for tempCode in tempCodeList :
                tempStock = stock.objects.get(stockCode=tempCode)
                tempRate = (tempStock.now - int(tempNowList[i])) / 100
                rate += tempRate
                i = i + 1
        except:
            rate = 0
            print("rate error")

        rate = rate / 3
        print(rate)

        return dict(
            url=self.url,
            title=self.title,
            leadingPeriod = self.leadingPeriod,
            leadingType = self.leadingType,
            stockNum=self.stockNum,
            stockCode=self.stockCode,
            stockRate = rate)
#createDate=self.createDate.day


    def addStockCode(self):

        tempCodeList = self.stockCode.split(',')
        tempStockNow = ""

        for tempCode in tempCodeList :
            tempStock = stock(stockCode=tempCode, now=0 ,recommendNum=1)
            try:
                tempStock.save(force_insert=True)
                print("Save Stock")
            except:
                tempStock = stock.objects.get(stockCode=tempCode)
                tempRecommandNum = tempStock.recommendNum + 1
                tempStock.recommendNum = tempRecommandNum
                tempStock.save()
                print("Update Stock recommendNum")

            tempStockNow += tempStock.checkNow()+","

        self.stockNow = tempStockNow
        print("self.stockNow : " + self.stockNow)
        self.save()
        temp = self.stockNow.split(',')
        print(temp)
