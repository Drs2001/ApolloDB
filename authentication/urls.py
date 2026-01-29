from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login_page, name='login_page'), # Login page
    path('logout/', views.logout_page, name='logout'),
	path('register/', views.register_page, name='register'), # Registration page
]
