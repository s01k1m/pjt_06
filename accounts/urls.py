from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('delete/', views.delete, name='delete'),
    path('password/', views.change_password, name='change_password'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),

]