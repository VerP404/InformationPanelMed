from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('k1/', views.korpus_1, name='k1'),
    path('get_data_k1/', views.korpus_1_get_data, name='get_data_k1'),
    path('k2/', views.korpus_2, name='k2'),
    path('get_data_k2/', views.korpus_2_get_data, name='get_data_k2'),
    path('k3/', views.korpus_3, name='k3'),
    path('get_data_k3/', views.korpus_3_get_data, name='get_data_k3'),
    path('k6/', views.korpus_6, name='k6'),
    path('get_data_k6/', views.korpus_6_get_data, name='get_data_k6'),
    path('jk/', views.korpus_jk, name='jk'),
    path('get_data_jk/', views.korpus_jk_get_data, name='get_data_jk'),
    path('dp1/', views.korpus_dp1, name='dp1'),
    path('get_data_dp1/', views.korpus_dp1_get_data, name='get_data_dp1'),
    path('dp8/', views.korpus_dp8, name='dp8'),
    path('get_data_dp8/', views.korpus_dp8_get_data, name='get_data_dp8'),
    path('get_report_datetime/', views.get_report_datetime, name='get_report_datetime'),
    path('upload_data/', views.upload_data, name='upload_data'),
]
