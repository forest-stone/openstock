from django.shortcuts import render
from django.http import HttpResponse
import json
from stockScreener.models import stock
from .models import item


# Create your views here.
def showlist(request):
    results = [item.showitem() for item in item.objects.all()]
    return HttpResponse(json.dumps(results, indent=4), content_type="application/json")

#    return HttpResponse("<h1>this is the new list.</h1>")
def parsingJson(request):

  try:
    jsonString = request.GET['JSON']
    print (jsonString)
    dict = json.loads(jsonString)
    print ("Create URL data")
    print(dict['url'])
    print(dict['title'])
    print(dict['leadingPeriod'])
    print(dict['leadingType'])
    print(dict['stockNum'])
    print(dict['stockCode'])   
# print(dict['url'] + " | " + dict["title"] + " | " + dict["leadingPeriod"]
#          + " | " + dict["leadingType"] + " | " + dict['stockNum'] + " | " + dict['stockCode'])
  except:
    print("Json error")
    # json error code : 2
    return HttpResponse("2")

  itemTemp = item(url=dict['url'], title=dict["title"], leadingPeriod=dict['leadingPeriod'],
  leadingType=dict['leadingType'], stockNum=dict['stockNum'], stockCode=dict['stockCode'])

  try:
    itemTemp.save(force_insert=True)
  except:
    print("URL already exist")
    # already exist(URL) code : 3
    return HttpResponse("3")

  # create success code : 1
  itemTemp.addStockCode()
  return HttpResponse("1")
