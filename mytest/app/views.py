import json
from django.shortcuts import render
from django.views.generic import View
from app import models
from app import core

# Create your views here.

# 用户上传信息
class InfoUpload(View):
    '''
    method:post
    params:name,age,tem,place
    success：code 6200  msg  成功添加至数据库
    fail： code  6201   msg  用户输入不完整
    Description：将用户输入的相关信息添加至数据库
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
            code = 6201
        else:
            info = models.UserInfo(name=name,age=age,tem=tem,place=place)
            info.save()
            msg = '上传成功'
            code = 6200
        return render(request,'app/info.html',locals())
