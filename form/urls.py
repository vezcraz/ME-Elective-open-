from django.urls import path
# from django.contrib.auth.views import login
from django.contrib.auth import login
from . import views

urlpatterns = [
	# path('', views.home.as_view(), name='blog-home'), use as_view for class based view
	# path('login/',login, {'template_name': '/login.html'}, name='login')
]
