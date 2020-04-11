from django.db import models

# Create your models here.

# 抽象基类
class Base(models.Model):
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')  # 创建时自动生成
    update_time = models.DateTimeField(auto_now=True,verbose_name='更新时间')    # 更新时自动记录时间
    class Meta:
        abstract = True


# 用户信息表
class UserInfo(Base,models.Model):
    '''
    都是必填项，不设置默认值
    '''
    name = models.CharField(max_length=20,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    tem = models.DecimalField( max_digits=4, decimal_places=2,verbose_name='体温')
    place = models.CharField(max_length=40,verbose_name='位置')
    class Meta:
        db_table = 'userinfo'
