from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Описание проекта:
def index(request):
    username = request.user.get_username()
    return render(request, 'index.html', {'username': username})

#Методика:
def methodics(request):
    username = request.user.get_username()
    return render(request, 'description/methodics.html', {'username': username})

#Контроль результатов:
def results_control(request):
    username = request.user.get_username()
    return render(request, 'description/results_control.html', {'username': username})

#Советы:
def advices(request):
    username = request.user.get_username()
    return render(request, 'description/advices.html', {'username': username})

# О пользователе:
@login_required
def about_user(request):
    username = request.user.get_username()
    user = User.objects.get(username=username)
    create_on = user.date_joined
    last_login = user.last_login
    return render(request, 'registration/about_user.html', {
        'username': username,
        'create_on': create_on,
        'last_login': last_login,
        'email': user.email})

def about(request):
    username = request.user.get_username()
    return render(request, 'about.html', {'username': username})

