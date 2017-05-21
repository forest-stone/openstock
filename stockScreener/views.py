from django.shortcuts import render
from .models import stock
import time


# Create your tests here.
stopScreen = False

def getStockNow(request):
    while(1) :
        if(stopScreen)
            break

        time.sleep(10)
        print("getStockNow - start")
        for stocktemp in stock.objects.all() :
            stocktemp.checkStockNow()


def getStockMA(request):
        print("getStockMA - start")
        for stocktemp in stock.objects.all() :
                stocktemp.checkStockMA()

"""
    stockItem = '119500'

    url = 'http://finance.daum.net/item/quote_avg_yyyymmdd_sub2.daum?code=' + stockItem
    html = urlopen(url)
    source = BeautifulSoup(html.read(), "html.parser")
    srlists=source.find_all("tr")
    isCheckNone = None

    if(srlists[2].span != isCheckNone):
        #print(srlists[2])
        #print(srlists[2].find_all("td",class_="datetime2")[0].text) #날짜
        print(srlists[2].find_all("td",class_="num")[3].text) #5일선
        #print(srlists[2].find_all("td",class_="num")[4].text) #10일선
        print(srlists[2].find_all("td",class_="num")[5].text) #20일선
        print(srlists[2].find_all("td",class_="num")[6].text) #60일선
        #print(srlists[2].find_all("td",class_="num")[7].text) #120일선

# Create your views here.
"""
