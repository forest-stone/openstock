from django.shortcuts import render
from django.http import HttpResponse
import json
from stockScreener.models import stock
from .models import item


# Create your views here.
def showlist(request):
    item.objects.order_by('createDate')
    results = [item.as_json() for item in item.objects.all()]
    return HttpResponse(json.dumps(results, indent=4), content_type="application/json")

#    return HttpResponse("<h1>this is the new list.</h1>")


def parsingJson(request):

  try:
    jsonString = request.GET['JSON']
    print (jsonString)
    # 테스트용 JSON 문자열
    # JSON 디코딩
    dict = json.loads(jsonString)
    print (dict)
    # Dictionary 데이타 체크
    print(dict["title"])
    print(dict['url'])
    print(dict['stockNum'])
    print(dict['stock1Code'])
    print(dict['stock2Code'])
    print(dict['stock3Code'])
  except:
    print("Json없다 다시 시도해봐라")
    return HttpResponse("Json없다 다시 시도해봐라")

  itemTemp = item(title=dict["title"], url=dict['url'], stockNum=dict['stockNum'],
  stock1Code=dict['stock1Code'], stock2Code=dict['stock2Code'], stock3Code=dict['stock3Code'])

  try:
    itemTemp.save(force_insert=True)
  except:
    print("이미있다임마")
    return HttpResponse("이미있다임마")

  return HttpResponse("정상등록!"+dict["title"])
