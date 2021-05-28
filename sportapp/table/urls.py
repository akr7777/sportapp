from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from . import registration
from . import params

app_name = 'sport'

urlpatterns = [
    path("table1/", views.index_table, name="table1"),
    path("table2/", views.table2, name="table2"),
    #path("table2/save_percents/", views.table2_save_percents, name="table2_save_percents"),
    path("add_new/", views.add_new, name="add_new"),
    #path("parcheck/", params.parcheck, name="parcheck"),
    path("add_new/del_heart_rate", params.del_heart_rate, name="del_heart_rate"),
    path("add_new/new_heart_rate", params.new_heart_rate, name="new_heart_rate"),
    path("add_new/new_method", params.new_method, name="new_method"),
    path("add_new/del_method", params.del_method, name="del_method"),
    #path("edit_table_by_user", views.edit_table_by_user, name="edit_table_by_user"),
    #re_path(r'^edit_table_by_user/(?P<value>\d+)/(?P<col_id>\D+)/(?P<row_name>\D+)/', views.edit_table_by_user),
    path('edit_table_by_user/<value>/<col_id>/<row_name>/', views.edit_table_by_user),
    path("new/", registration.new_user_registration, name="new_registration"),
]