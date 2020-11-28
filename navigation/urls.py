from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('interface_tool/',views.interface_tool,name='interface_tool')
]

