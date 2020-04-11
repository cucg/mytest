import datetime
import csv
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
    # 每天以覆盖的方式写入
    with open('userinfo.csv','w+',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=' ')
        writer.writerow(['体温','人数'])
        for i in info:
            writer.writerow([i['tem'],i['number']])
    # 发送邮件
    subject = '体温检测报告'  # 标题部分
    message = ''.join((nowDate ,'的体温报告')) # 主题部分
    recv_email = '814972189@qq.com'
    email = mail.EmailMessage(subject, message,settings.DEFAULT_FROM_EMAIL, [recv_email])
    # 选择附件发送
    email.attach_file('userinfo.csv')
    email.send()
