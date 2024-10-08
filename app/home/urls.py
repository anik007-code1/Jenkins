from django.urls import path
from .views import category_list, category_detail, books_by_category, PDFDetailView, register, login, logout

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<slug:slug>/', category_detail, name='category_detail'),
    path('category/<slug:slug>/books/', books_by_category, name='books_by_category'),
    path('pdf/<slug:slug>/', PDFDetailView, name='pdf_detail'),  # Ensure this line is present
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
