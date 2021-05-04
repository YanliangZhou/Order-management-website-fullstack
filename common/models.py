from django.db import models
import datetime

# Create your models here.
# class Customer(models.Model):
#     #客户名称
#     name = models.CharField(max_length=200)
#
#     #联系电话
#     phonenumber = models.CharField(max_length=200)
#
#     #地址
#     address = models.CharField(max_length=200)
#
#
# class Medicine(models.Model):
#     # 药品名
#     name = models.CharField(max_length=200)
#     # 药品编号
#     sn = models.CharField(max_length=200)
#     # 描述
#     desc = models.CharField(max_length=200)


class Order(models.Model):
    # # 订单名
    # name = models.CharField(max_length=200,null=True,blank=True)

    # # Date
    # create_date = models.DateTimeField(default=datetime.datetime.now)
    id = models.AutoField(primary_key=True)
    time = models.CharField(max_length=200,default="")
    # time = models.CharField(max_length=200,default="",primary_key=True)
    # time = models.DateTimeField(auto_now=False, auto_now_add=False, default="")
    side = models.CharField(max_length=200,default="")
    qty = models.IntegerField(default="")
    symbol = models.CharField(max_length=200,default="")
    px = models.IntegerField(default="")
    exchange = models.CharField(max_length=200,default="")
    class_type = models.CharField(max_length=200,default="")
    description = models.CharField(max_length=200,default="")
    tags = models.CharField(max_length=200,default="")
    local_time = models.CharField(max_length=200,default="")
    source = models.CharField(max_length=200,default="")
    orderID = models.CharField(max_length=200,default="")
    exchangeOID = models.CharField(max_length=200,default="")
    fillID = models.CharField(max_length=200,default="")
    strategy = models.CharField(max_length=200,default="")
    ilink = models.CharField(max_length=200,default="")
    px_multiplier = models.CharField(max_length=200,default="")
    multiplier = models.CharField(max_length=200,default="")
    TO = models.CharField(max_length=200,default="")
    OC = models.CharField(max_length=200,default="")

    # def __str__(self):
    #     return self.time


# class OrderMedicine(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT)
#     medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
#
#     # 订单中药品的数量
#     amount = models.PositiveIntegerField()


#
# from django.contrib import admin
# admin.site.register(Customer)
#
#
# # 国家表
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#
# # 学生表， country 字段是国家表的外键，形成一对多的关系
# class Student(models.Model):
#     name    = models.CharField(max_length=100)
#     grade   = models.PositiveSmallIntegerField()
#     country = models.ForeignKey(Country,
#                                 on_delete=models.PROTECT)