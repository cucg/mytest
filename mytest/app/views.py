import json
from django.shortcuts import render
from django.views.generic import View
from django.db.models import Count
from app import models


# Create your views here.

# 用户上传信息
class InfoUpload(View):
    '''
    method:post
    params:name,age,tem,place
    '''
    def get(self,request):
        return render(request,'app/info.html')
    def post(self,request):
        name = request.POST['name']
        age = request.POST['age']
        tem = request.POST['tem']
        place = request.POST['place']
        # 先判断用户输入是否完整
        if not all([name,age,tem,place]):
            msg = '请输入完整'
        else:
            info = models.UserInfo(name=name,age=age,tem=tem,place=place)
            info.save()
            msg = '上传成功'
        return render(request,'app/info.html',locals())


