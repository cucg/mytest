# Generated by Django 2.0.4 on 2020-04-11 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0002_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('tem', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='体温')),
                ('place', models.CharField(max_length=40, verbose_name='位置')),
            ],
            options={
                'db_table': 'userinfo',
            },
        ),
    ]