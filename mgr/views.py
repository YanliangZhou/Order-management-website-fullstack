from django.shortcuts import render
from django.http import HttpResponse
from common.models import Order
from django import forms
import csv, io, os
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from tkinter import *
import tkinter.messagebox
from django.views.generic import View
import pandas as pd
import numpy as np


# Create your views here.


# def home(request):
#     import json
#     # api_request = Order.objects.values()
#     # api = json.loads(api_request.content)
#     qs = Order.objects.values()
#     return render(request, 'orders.html', {'api': qs})


def home(request):
    return render(request, 'home.html')


def listorders(request):
    # # 根据session判断用户是否是登录的管理员用户
    # if 'usertype' not in request.session:
    #     return JsonResponse({
    #         'ret': 302,
    #         'msg': '未登录',
    #         'redirect': '/mgr/sign.html'},
    #         status=302)
    #
    # if request.session['usertype'] != 'mgr':
    #     return JsonResponse({
    #         'ret': 302,
    #         'msg': '用户非mgr类型',
    #         'redirect': '/mgr/sign.html'},
    #         status=302)

    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Order.objects.values()

    # 检查url中是否有参数phonenumber
    time_info = request.GET.get('search_time', None)
    side_info = request.GET.get('search_side', None)
    qty_info = request.GET.get('search_qty', None)
    symbol_info = request.GET.get('search_symbol', None)
    price_info = request.GET.get('search_price', None)
    exchange_info = request.GET.get('search_exchange', None)
    strategy_info = request.GET.get('search_strategy', None)
    ilink_info = request.GET.get('search_ilink', None)
    traderowner_info = request.GET.get('search_trader-owner', None)

    # 如果有，添加过滤条件
    # if time_info:
    #     qs = qs.filter(Q(time=info)|Q(side=info)|Q(qty__lt=info)|Q(symbol=info)|Q(px=info)|Q(exchange=info)|Q(strategy=info)|Q(ilink=info)|Q(TO=info))
    #     # for i in (time,side,qty,symbol,)
    #     # qs = qs.filter(time=rt)

    if time_info:
        status = False
        n = len(time_info)
        for i in range(n):
            if time_info[i] == ' ':
                qs = qs.filter(Q(time__range=[time_info[0:i], time_info[i+1:n]]))
                status = True
        if status == False:
            qs = qs.filter(Q(time__contains=time_info))
    if side_info:
        qs = qs.filter(Q(side=side_info))
    if qty_info:
        status = False
        n = len(qty_info)
        for i in range(n):
            if qty_info[i] == ' ':
                qs = qs.filter(Q(qty__range=[int(qty_info[0:i]), int(qty_info[i+1:n])]))
                status = True
        if status == False:
            qs = qs.filter(Q(qty=qty_info))
    if symbol_info:
        qs = qs.filter(Q(symbol=symbol_info))
    if price_info:
        status = False
        n = len(price_info)
        for i in range(n):
            if price_info[i] == ' ':
                qs = qs.filter(Q(px__range=[price_info[0:i], price_info[i + 1:n]]))
                status = True
        if status == False:
            qs = qs.filter(Q(px=price_info))
    if exchange_info:
        qs = qs.filter(Q(exchange=exchange_info))
    if strategy_info:
        qs = qs.filter(Q(strategy=strategy_info))
    if ilink_info:
        qs = qs.filter(Q(ilink=ilink_info))
    if traderowner_info:
        qs = qs.filter(Q(TO=traderowner_info))


    # rsd = request.GET.get('side', None)
    # # 如果有，添加过滤条件
    # if rsd:
    #     qs = qs.filter(side=rsd)
    #
    # rq = request.GET.get('search_info', None)
    # # 如果有，添加过滤条件
    # if rq:
    #     qs = qs.filter(qty=rq)

    # rsb = request.GET.get('symbol', None)
    # # 如果有，添加过滤条件
    # if rsb:
    #     qs = qs.filter(symbol=rsb)
    #
    # rp = request.GET.get('px', None)
    # # 如果有，添加过滤条件
    # if rp:
    #     qs = qs.filter(px=rp)
    #
    # re = request.GET.get('exchange', None)
    # # 如果有，添加过滤条件
    # if re:
    #     qs = qs.filter(exchange=re)
    #
    # rst = request.GET.get('strategy', None)
    # # 如果有，添加过滤条件
    # if rst:
    #     qs = qs.filter(strategy=rst)
    #
    # ri= request.GET.get('ilink', None)
    # # 如果有，添加过滤条件
    # if ri:
    #     qs = qs.filter(ilink=ri)
    #
    # rto = request.GET.get('TO', None)
    # # 如果有，添加过滤条件
    # if rto:
    #     qs = qs.filter(TO=rto)

    # 生成html模板中要插入的html片段内容
    tableContent = ''
    # i = 0
    # for order in qs:
    #     if i == 0:
    #         i += 1
    #         continue
    #     else:
    #         tableContent += '<tr>'
    #         for name, value in order.items():
    #             tableContent += f'<td>{value}</td>'
    #         tableContent += '</tr>'
    # i = 0
    for order in qs:
        tableContent += '<tr>'
        for name, value in order.items():
            tableContent += f'<td>{value}</td>'
        tableContent += '</tr>'

    # return HttpResponse(html_template % tableContent)
    return render(request, 'orders.html', {'order_list': qs})


# def upload(request):
#     return render(request, 'upload.html')


class order_form(forms.Form):
    Browse = forms.FileField()

# def file_upload(request):
#     # 根据session判断用户是否是登录的管理员用户
#     if 'usertype' not in request.session:
#         return JsonResponse({
#             'ret': 302,
#             'msg': '未登录',
#             'redirect': '/mgr/sign.html'},
#             status=302)
#
#     if request.session['usertype'] != 'mgr':
#         return JsonResponse({
#             'ret': 302,
#             'msg': '用户非mgr类型',
#             'redirect': '/mgr/sign.html'},
#             status=302)


# def file_upload(request):
#     if request.method == "POST":
#         uf = request.FILES.get("uf",None)
#         # print("myfile", myfile)
#         # check if it's a csv file
#         # if not uf.name.endswith('.csv'):
#         #     message.error(request, 'This is not a csv file')
#         if uf:
#             # uf.name = "uploaded_data"
#             # destination = open(os.path.join("/home/yanliangzhou/PycharmProjects/Python3/djangoProject/mgr/data/%s" % myfile.name),'wb+')
#             # for chunk in myfile.chunks():
#             #     destination.write(chunk)
#             # destination.close()
#             # csvdata = convert_to_csv(destination)
#
#             df = pd.DataFrame(uf)
#             df.to_csv("/home/yanliangzhou/PycharmProjects/Python3/djangoProject/mgr/data/data.csv", sep=',', header=True, index=False)
#             with open("/home/yanliangzhou/PycharmProjects/Python3/djangoProject/mgr/data/data.csv", 'r',encoding='utf-8') as f:
#                 csvdata = csv.reader(f)
#             data = csvdata.cleaned_data['Browse']
#             data_set = data.read().decode('UTF-8')
#             io_string = io.StringIO(data_set)
#             next(io_string)
#             for column in csv.reader(io_string, delimiter=',', quotechar="|"):
#                 if column[0] == "":
#                     continue
#                 _, created = Order.objects.update_or_create(
#                     time=column[0],
#                     side=column[1],
#                     qty=column[2],
#                     symbol=column[3],
#                     px=column[4],
#                     exchange=column[5],
#                     class_type=column[6],
#                     description=column[7],
#                     tags=column[8],
#                     local_time=column[9],
#                     source=column[10],
#                     orderID=column[11],
#                     exchangeOID=column[12],
#                     fillID=column[13],
#                     strategy=column[14],
#                     ilink=column[15],
#                     px_multiplier=column[16],
#                     multiplier=column[17],
#                     TO=column[18],
#                     OC=column[19]
#                 )
#             context = {}
#             messages.error(request, "Upload Successfully!")
#             # return HttpResponse('Upload OK!')
#     else:
#         uf = order_form()
#     return render(request, 'upload.html', {'uf': uf})



def file_upload(request):
    if request.method == "POST":
        uf = order_form(request.POST, request.FILES)
        # check if it's a csv file
        # if not uf.name.endswith('.csv'):
        #     message.error(request, 'This is not a csv file')
        # csvdata = uf.convert_to_csv(uf)
        if uf.is_valid():
            data = uf.cleaned_data['Browse']
            data_set = data.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                if column[0] == "":
                    continue
                _, created = Order.objects.update_or_create(
                    # time=column[0][0:4]+'-'+column[0][4:6]+'-'+column[0][6:8]+' '+column[0][9:24],
                    time=column[0],
                    side=column[1],
                    qty=column[2],
                    symbol=column[3],
                    px=column[4],
                    exchange=column[5],
                    class_type=column[6],
                    description=column[7],
                    tags=column[8],
                    local_time=column[9],
                    source=column[10],
                    orderID=column[11],
                    exchangeOID=column[12],
                    fillID=column[13],
                    strategy=column[14],
                    ilink=column[15],
                    px_multiplier=column[16],
                    multiplier=column[17],
                    TO=column[18],
                    OC=column[19]
                )
            context = {}
            messages.error(request, "Upload Successfully!")
            # return HttpResponse('Upload OK!')
    else:
        uf = order_form()
    return render(request, 'upload.html', {'uf': uf})


    # csv_file = request.FILES['files']
    #
    # #check if it's a csv file
    # if not csv_file.name.endswith('.csv'):
    #     message.error(request, 'This is not a csv file')
    #
    # data_set = csv_file.read().decode('UTF-8')
    # io_string = io.StringIO(data_set)
    # next(io_string)
    # for column in csv.reader(io_string, delimiter=',', quotechar="|"):
    #     _, created = Order.objects.update_or_create(
    #     time=column[0],
    #     side = column[0],
    #     qty = column[0],
    #     symbol = column[0],
    #     px = column[0],
    #     exchange = column[0],
    #     class_type = column[0],
    #     description = column[0],
    #     tags = column[0],
    #     local_time = column[0],
    #     source = column[0],
    #     orderID = column[0],
    #     exchangeOID = column[0],
    #     fillID = column[0],
    #     strategy = column[0],
    #     ilink = column[0],
    #     px_multiplier = column[0],
    #     multiplier = column[0],
    #     TO = column[0],
    #     OC = column[0]
    #     )
    # context = {}
    # return render_to_response(request, html_template, context)
    # return render(request, 'upload.html', {})


def convert_to_csv(data):
    with open(os.path.join('/home/yanliangzhou/PycharmProjects/Python3/djangoProject/mgr/data', 'data.csv'), 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        with open(data) as filein:
            for line in filein:
                line_list = line.strip('\n').split('\n')
                for colum in line_list:
                    columtxt = colum.strip('\n').split('\t')
                    spamwriter.writerow(columtxt)
    return spamwriter