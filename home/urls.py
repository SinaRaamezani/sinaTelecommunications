from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('home/' , views.user_list , name = 'home'),
    path('search/' , views.search_user , name = 'serachuser'),
]
