import os
import datetime
import xlwt
from app import models
from django.core import mail
from django.db.models import Count
from mytest import settings
# 定时执行的任务
def task():
    # 获取当前日期
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    # 使用annotate对tem字段进行分组并统计其出现的次数
    info = models.UserInfo.objects.values('tem').annotate(number=Count('tem')).values('tem','number').filter(create_time__gt=nowDate)
    fileName = 'userinfo.xlsx'
    excel = xlwt.Workbook(encoding="utf-8")
    sheet = excel.add_sheet('Sheet1')
    sheet.write(0,0,'体温')	# 不带样式的写入
    sheet.write(0,1,'人数')
    flag = 1
    for i in info:
        sheet.write(flag,0,i['tem'])
        sheet.write(flag,1,i['number'])
        flag += 1
    # 将写入的数据保存至文件
    FilePath = os.path.join(settings.BASE_DIR,fileName)
    excel.save(FilePath)
    # 发送邮件
    subject = '体温检测报告'  # 标题部分
    message = ''.join((nowDate ,'的体温报告')) # 主题部分
    recv_email = '814972189@qq.com'  # 指定邮箱接收
    email = mail.EmailMessage(subject, message,settings.DEFAULT_FROM_EMAIL, [recv_email])
    # 选择附件发送
    email.attach_file(FilePath)
    email.send()
