#-*- coding: utf-8 -*-
from django.http import HttpResponse
import json,codecs

#获取前端post到接口的数据
def hello(request):
    name=request.REQUEST["name"]
    hobby=request.REQUEST["hobby"]
    age=request.REQUEST["age"]
    dict=[{"name":name,"hobby":hobby,"age":age}]
    data={'data':dict}
    data=json.dumps(data)
    with open('data.txt', 'wb') as f:
        json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
    return HttpResponse(data)

def myage(request):
    return HttpResponse("我的年龄是"+str(23))

