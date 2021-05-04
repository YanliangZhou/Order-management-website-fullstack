from django.urls import path, re_path
# from mgr import customer
from . import sign_in_out
# from mgr import medicine
from .views import listorders, file_upload, home

from django import urls
from django.conf.urls import url

urlpatterns = [
    # path('', home,name="home"),
    # path('orders/', listorders),
    # path('customers', customer.dispatcher),
    # path('medicines', medicine.dispat cher),
    path('signin', sign_in_out.signin),
    path('signout', sign_in_out.signout),
    # url(r'^file_upload$', file_upload, name='file_upload'),
]
