import csv 
from app import models
# 定时执行的任务
def task():
    # 使用annotate对tem字段进行分组并统计其出现的次数
    info = models.UserInfo.objects.values('tem').annotate(number=Count('tem')).values('tem','number')
    print(info)
    # 每天以覆盖的方式写入
    with open('userinfo.csv','w+',encoding='utf-8') as f:
            writer = csv.writer(f,delimiter=' ')
            writer.writerow(['体温','人数'])
            writer.writerow([])