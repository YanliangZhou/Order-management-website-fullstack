"""managewebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from mgr import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('sales/', include('sales.urls')),
    path('mgr/', include('mgr.urls')),
    path('api/mgr/', include('mgr.urls')),
    path('upload/', views.file_upload, name="upload"),
    path('orders/', views.listorders, name="list_order"),
    path('home/', views.home, name="home"),
    path('', views.home,name="home"),
]
# ] +  static("/", document_root="./z_dist1")
urlpatterns += staticfiles_urlpatterns()