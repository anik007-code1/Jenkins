from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name="logout"),
    path('', views.home, name='home'),
    path('pdf/<slug:slug>/', views.PDFDetailView, name='pdf_detail'),

]

