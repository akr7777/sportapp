# coding: utf-8
import os

from django.shortcuts import render
from .models import Results, Methods, Heart_rates
from django.urls import path
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from ._function import get_table_top, get_table_context, get_table_bottom, months_list, get_table_context_json
from ._function import months_list, get_table_context_json, save_new_result_from_user_table
#from ._function import save_new_result_from_user_table
from ._function import get_context_for_table_2, latest_rows_context
import datetime
import json

# Таблица с результатами:
@login_required
def index_table(request):

    username = request.user.get_username()
    user = User.objects.get(username=username)
    now = datetime.datetime.now()
    year = now.year
    years = [year-3, year-2, year-1, year]
    month = now.month
    month_str = months_list[month - 1]

    if request.method == 'POST':
        year = int(request.POST.get("select_year_table"))
        month = 1 + months_list.index(request.POST.get("select_month_table"))
        month_str = months_list[month - 1]

    json_table_context = get_table_context_json(user, year, month)

    methods = Methods.objects.filter(user_id=user)

    cont = {
                    'years': years,
                    'current_year': year,
                    'months': months_list,
                    'current_month': month_str,
                    'username': username,
                    'json_table_context': json_table_context,
                    'methods': methods
                  }
    return render(request, 'table/table_1.html', cont)

# Добавить результат:
@login_required
def add_new(request):
    username = request.user.get_username()
    user = User.objects.get(username=username)
    result_added = ''
    if request.method == 'POST':
        result = Results()
        result.user_id = user
        result.date = request.POST.get("input_date")

        heart_rate_id = Heart_rates.objects.get(heart_interval=request.POST.get("select_heart_rate"),
                                                user_id=user)
        result.heart_rate_id = heart_rate_id

        method_id = Methods.objects.get(method_name=request.POST.get("select_method"),
                                        user_id=user)
        result.method_id = method_id

        result.result = request.POST.get("input_result")
        result.save()
        result_added = 'Результат добавлен!'

    heart_rates = Heart_rates.objects.filter(user_id=user)
    methods = Methods.objects.filter(user_id=user)
    today = datetime.datetime.now()
    return render(request, 'table/add_new.html',
                  {'username': username,
                   'today': today,
                   'heart_rates': heart_rates,
                   'methods': methods,
                   'result_added': result_added
                   })

def edit_table_by_user(request, value, col_id, row_name):
    username = request.user.get_username()
    user = User.objects.get(username=username)
    today = datetime.datetime.now()
    if " " in value:
        value_list = value.split(" ")
        for val in value_list:
            save_new_result_from_user_table(user, today, val, col_id, row_name)
    else:
        save_new_result_from_user_table(user, today, value, col_id, row_name)

    return HttpResponseRedirect("/table/table1")

@login_required
def table2(request):
    username = request.user.get_username()
    user = User.objects.get(username=username)
    now = datetime.datetime.now()
    year = now.year
    years = [year - 3, year - 2, year - 1, year]
    month = now.month
    month_str = months_list[month - 1]
    methods = Methods.objects.filter(user_id=user)
    rates = Heart_rates.objects.filter(user_id=user)

    if request.method == 'POST':

        if request.POST.get("select_year_table") != None:
            year = int(request.POST.get("select_year_table"))
        if request.POST.get("select_month_table") != None:
            month = 1 + months_list.index(request.POST.get("select_month_table"))
            month_str = months_list[month - 1]

        json_text = {}
        if request.POST.get("input_total_time") != None:
            json_text['total_time'] = int(request.POST.get("input_total_time"))

            year = int(request.POST.get("choosen_year"))
            month = 1 + months_list.index(request.POST.get("choosen_month"))
            month_str = months_list[month - 1]

            for rate in rates:
                field_name = str(rate.heart_interval)
                value = int(request.POST.get("input_rate_" + rate.heart_interval))
                json_text[field_name] = value
            for meth in methods:
                field_name = str(meth.method_name)
                value = int(request.POST.get("input_meth_" + meth.method_name))
                json_text[field_name] = value

            #Сохраняем в файл:
            data_to_save = json.dumps(json_text)
            filename = username+"_"+str(year)+"_"+str(month)+".t2d"
            path_to_file = os.path.join(os.getcwd(), 'files', filename)
            file1 = open(path_to_file, "w")
            file1.write(data_to_save)
            file1.close()

    context1 = get_context_for_table_2(user, year, month)
    bottom_context_1 = latest_rows_context(user, year, month)[0]
    bottom_context_2 = latest_rows_context(user, year, month)[1]

    cont = {
        'years': years,
        'current_year': year,
        'months': months_list,
        'current_month': month_str,
        'username': username,
        'methods': methods,
        'rates': rates,
        'context1': context1,
        'bottom_context_1': bottom_context_1,
        'bottom_context_2': bottom_context_2
    }
    return render(request, 'table/table_2.html', cont)

