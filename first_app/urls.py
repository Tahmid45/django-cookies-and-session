
from django.urls import path
from . import views
urlpatterns = [
    path('', views.set_session, name='homepage'),
    path('cookies/', views.get_cookie),
    path('del_cookies/', views.delete_session),
    path('get_session/', views.get_session),
]
