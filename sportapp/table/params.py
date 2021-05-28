from django.contrib.auth.models import User
from .models import Heart_rates, Methods
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Редактирование параметров
@login_required
def parcheck(request):
    username = request.user.get_username()
    user = User.objects.get(username=username)
    heart_rates = Heart_rates.objects.filter(user_id=user)
    methods = Methods.objects.filter(user_id=user)
    return render(request, 'table/params.html', {
        'username': username,
        'heart_rates': heart_rates,
        'methods': methods
    })

def del_heart_rate(request):
    #print('\n\nУдаление ЧСС\n\n')
    if request.method == 'POST':
        username = request.user.get_username()
        user = User.objects.get(username=username)
        heart_rate_for_delete = request.POST.get("del_heart_rate_select")
        h_rate = Heart_rates.objects.filter(user_id=user, heart_interval=heart_rate_for_delete)
        h_rate.delete()
    return HttpResponseRedirect("/table/add_new/")

def new_heart_rate(request):
    #print('\n\nДобавление нового ЧСС\n\n')
    if request.method == "POST":
        username = request.user.get_username()
        user = User.objects.get(username=username)
        heart_rate_for_add = request.POST.get("add_new_heart_rate_input")
        h_rate = Heart_rates()
        h_rate.user_id=user
        h_rate.heart_interval=heart_rate_for_add
        h_rate.save()
    return HttpResponseRedirect("/table/add_new/")

def new_method(request):
    #print('\n\nДобавление нового средства тренировок\n\n')
    if request.method == 'POST':
        username = request.user.get_username()
        user = User.objects.get(username=username)
        meth_add = request.POST.get("add_new_method_input")
        m = Methods()
        m.user_id = user
        m.method_name = meth_add
        m.save()
    return HttpResponseRedirect("/table/add_new/")

def del_method(request):
    #print('\n\nУдаление средства тренировок\n\n')
    if request.method == "POST":
        username = request.user.get_username()
        user = User.objects.get(username=username)
        mth_del = request.POST.get("del_method_select")
        h_rate = Methods.objects.filter(user_id=user, method_name=mth_del)
        h_rate.delete()
    return HttpResponseRedirect("/table/add_new/")