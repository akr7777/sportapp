# coding: utf-8
from .models import Results, Methods, Heart_rates
from django.contrib.auth.models import User
import json
import table.make_script_t1, table.make_script_t1_v2
import datetime
import os

months_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']

def get_total(user, year, month):
    summ = 0
    results = Results.objects.filter(user_id=user, date__year=year, date__month=month)
    for res in results:
        summ += res.result
    return summ

def get_heart_rate_total(user, year, month, heart_rate_id):
    summ = 0
    results = Results.objects.filter(user_id=user, date__year=year, date__month=month, heart_rate_id=heart_rate_id)
    for res in results:
        summ += res.result
    return summ

def get_method_total(user, year, month, method_id):
    summ = 0
    results = Results.objects.filter(user_id=user, date__year=year, date__month=month, method_id=method_id)
    for res in results:
        summ += res.result
    return summ


def get_table_top(user):
    meths = Methods.objects.filter(user_id=user)
    res = ['N', 'ЧСС']
    for item in meths:
        res.append(item)
    res.append('ИТОГО')
    res.append('%')
    return res

'''def get_table_context(user, year, month):
    context = []
    all_heart_rates = Heart_rates.objects.filter(user_id=user)
    number = 0
    for rate in all_heart_rates:
        line_context = []
        number += 1
        line_context.append(str(number))
        line_context.append(rate)
        #row = Results.objects.filter(user_id=user, heart_rate_id=rate, date__year=year, date__month=month)
        methods = Methods.objects.filter(user_id=user)
        for method in methods:
            cell_results = Results.objects.filter(user_id=user, heart_rate_id=rate,
                                                  date__year=year, date__month=month, method_id=method)
            cell = ''
            for cell_result in cell_results:
                cell += str(cell_result.result) + ' '
            line_context.append(cell)

        h_rate_total = get_heart_rate_total(user, year, month, rate)
        line_context.append(str(h_rate_total))
        if get_total(user, year, month) != 0:
            percent = str(100*h_rate_total/get_total(user, year, month))
            if len(percent) > 5:
                percent = percent[0:5]
        else:
            percent = '0'

        line_context.append(percent+'%')

        context.append(line_context)

    return context'''


def get_table_context_json(user, year, month):
    context = []
    all_heart_rates = Heart_rates.objects.filter(user_id=user)
    number = 0
    for rate in all_heart_rates:
        line_context = '{'
        number += 1
        line_context += '"number": "' + str(number) + '",'
        line_context += '"rate": "' + str(rate) + '",'
        methods = Methods.objects.filter(user_id=user)
        for method in methods:
            cell_results = Results.objects.filter(user_id=user, heart_rate_id=rate,
                                                  date__year=year, date__month=month, method_id=method)
            cell = ' '
            for cell_result in cell_results:
                cell += str(cell_result.result) + ' '
            #line_context.append(cell)
            line_context += '"'+str(method.id)+'": "' + str(cell) + '",'

        h_rate_total = get_heart_rate_total(user, year, month, rate)
        #line_context.append(str(h_rate_total))
        line_context += '"h_rate_total": "' + str(str(h_rate_total)) + '",'

        if get_total(user, year, month) != 0:
            percent = str(100*h_rate_total/get_total(user, year, month))
            if len(percent) > 5:
                percent = percent[0:5]
        else:
            percent = '0'

        #line_context.append(percent+'%')
        line_context += '"rate_percent": "' + str(percent+'%') + '"}'

        row = json.loads(line_context)
        context.append(row)

    context.append(get_table_bottom_json(user, year, month)[0])
    context.append(get_table_bottom_json(user, year, month)[1])

    table.make_script_t1.make_t1(context, methods)
    #table.make_script_t1_v2.make_t1_2(context, methods)
    return context

'''def get_table_bottom(user, year, month):
    bottom = []
    bottom1 = ['', 'ИТОГО:']
    bottom2 = ['', '%']

    all_methods = Methods.objects.filter(user_id=user)
    for method in all_methods:
        summ_method = get_method_total(user, year, month, method)
        bottom1.append(str(summ_method))
        if get_total(user, year, month) != 0:
            percent = str(100 * summ_method / get_total(user, year, month))
            if len(percent) > 5:
                percent = percent[0:5]
        else:
            percent = '0'
        bottom2.append(percent+'%')

    bottom1.append(str(get_total(user, year, month)))
    bottom2.append('100%')
    bottom1.append('100%')
    bottom2.append('')

    bottom.append(bottom1)
    bottom.append(bottom2)
    return bottom'''

def get_table_bottom_json(user, year, month):
    bottom1 = '{"number": " ", "rate": "ИТОГО:",'
    bottom2 = '{"number": " ", "rate": "%",'

    all_methods = Methods.objects.filter(user_id=user)
    for method in all_methods:
        summ_method = get_method_total(user, year, month, method)
        bottom1 += '"'+str(method.id)+'": "' + str(summ_method) + '",'
        if get_total(user, year, month) != 0:
            percent = str(100 * summ_method / get_total(user, year, month))
            if len(percent) > 5:
                percent = percent[0:5]
        else:
            percent = '0'
        bottom2 += '"'+str(method.id)+'": "'+percent+'%",'

    bottom1 += '"h_rate_total": "'+str(get_total(user, year, month))+'",'
    bottom2 += '"h_rate_total": "100%",'
    bottom1 += '"rate_percent": "100%"}'
    bottom2 += '"rate_percent": " "}'

    return [json.loads(bottom1), json.loads(bottom2)]


def save_new_result_from_user_table(user, today, value, col_id, row_name):
    result = Results()
    result.user_id = user
    result.date = today.date()

    heart_rate_id = Heart_rates.objects.get(heart_interval=row_name,
                                            user_id=user)
    result.heart_rate_id = heart_rate_id

    method_id = Methods.objects.get(id=col_id,
                                    user_id=user)
    result.method_id = method_id

    result.result = value
    result.save()

def get_initial_user_data_for_table_2(user):
    all_methods = Methods.objects.filter(user_id=user)
    all_rates = Heart_rates.objects.filter(user_id=user)

    '''rate_percents = [10, 20, 10, 10, 20, 10, 10]
    method_percents = [20, 20, 20, 20, 20]'''

    data = {}
    for i in range(0, len(all_rates)):
        data[all_rates[i].heart_interval] = 100/len(all_rates)
    for i in range(0, len(all_methods)):
        data[all_methods[i].method_name] = 100/len(all_methods)

    data['total_time'] = 1000
    return data

def get_percents(user, year, month):
    username = user.username
    filename1 = username + "_" + str(year) + "_" + str(month) + ".t2d"
    if os.path.exists(
            os.path.join(os.getcwd(), 'files', filename1)
    ):
        file = os.path.join(os.getcwd(), 'files', filename1)
        percents = json.load(open(file, "r"))
    else:
        percents = get_initial_user_data_for_table_2(user)
    return percents

def get_context_for_table_2(user, year, month):
    percents = get_percents(user, year, month)

    rows = []

    rates = Heart_rates.objects.filter(user_id=user)
    methods = Methods.objects.filter(user_id=user)
    for rate in rates:
        row = {}
        row["rate"] = rate.heart_interval
        n = 0
        row['data'] = []
        #print('f 224 percents=', percents)
        for method in methods:
            n += 1
            #print("f 226 ", percents[method.method_name], type(percents[method.method_name]), percents["total_time"], type(percents["total_time"]))
            meth_total = percents[method.method_name] * percents["total_time"] / 100
            cell_value = meth_total * percents[rate.heart_interval] / 100
            row['data'].append(round(cell_value))
        rate_total = round( percents[rate.heart_interval] * percents["total_time"] / 100 )
        row['rate_total'] = rate_total
        row['rate_percent'] = round(percents[rate.heart_interval])

        rows.append(row)
    #print('f 236 rows=', rows)
    return rows

def latest_rows_context(user, year, month):
    percents = get_percents(user, year, month)

    rows = []

    latest_row_1 = {}
    latest_row_1['itogo'] = 'ИТОГО:'
    latest_row_1['data'] = []
    methods = Methods.objects.filter(user_id=user)
    for method in methods:
        meth_total = percents[method.method_name] * percents["total_time"] / 100
        latest_row_1['data'].append(round(meth_total))

    latest_row_1['total_time'] = percents["total_time"]
    latest_row_1['total_percent'] = "100%"


    rows.append(latest_row_1)

    latest_row_2 = {}
    latest_row_2['itogo'] = '%'
    latest_row_2['data'] = []
    methods = Methods.objects.filter(user_id=user)
    for method in methods:
        input_name = method.method_name
        percent = round(percents[method.method_name])
        latest_row_2['data'].append({'input_name': input_name, 'value': round(percent)})
        #latest_row_2['data']["value"] = round(percent)
        #latest_row_2[method.method_name] = percents[method.method_name]
        #latest_row_2[method.method_name] = method.method_name
    latest_row_2['total_time'] = "100%"
    latest_row_2['total_percent'] = " "

    rows.append(latest_row_2)

    return [rows[0], rows[1]]
'''def get_context_table_2(user, year, month):
    total = 1000
    #rate_percents = [10, 20, 10, 10, 20, 10, 10]
    #method_percents = [20, 20, 20, 20, 20]

    all_methods = Methods.object.filter

    rate_totals = {}
    for rate_percent in rate_percents:
        rate_totals[] = 100*rate_percent/total

    method_totals = {}
    for method_percent in method_percents:
        method_totals[] = 100*method_percent/total'''