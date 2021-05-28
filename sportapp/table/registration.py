from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Methods, Heart_rates

#Регистрация нового пользователя
def new_user_registration(request):
    if request.method == "POST":
        username1 = request.POST.get("login")
        password1 = request.POST.get("password")
        email1 = request.POST.get("email")

        if is_user_new(username1):
            User.objects.create_user(username1, email1, password1)
            create_rows_and_columns(User.objects.get(username=username1))
            return HttpResponseRedirect("/accounts/login")
        else:
            return render(request, 'registration/registration.html',
                          {'exist': 'Такой пользователь уже существует'})

    return render(request, 'registration/registration.html')

def is_user_new(username1):
    if User.objects.filter(username=username1).exists():
        return False
    else:
        return True

def create_rows_and_columns(user):
    heart_rates = ['>190', '170-190', '150-170', '130-150', '110-130']
    for rate_name in heart_rates:
        rate = Heart_rates()
        rate.user_id=user
        rate.heart_interval=rate_name
        rate.save()
    methods_names = ['Бег', 'Лыжи (своб)', 'Лыжи (класс)', 'Лыжи (имит)', 'ОФП ОРУ', 'ОФП спец.', 'Стрельба']
    for meth_name in methods_names:
        meth = Methods()
        meth.user_id = user
        meth.method_name = meth_name
        meth.save()