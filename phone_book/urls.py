from django.urls import path
from .views import *

urlpatterns = [
    path('api/getphonebooklist', PhoneBookList.as_view(), name='phone-book-list-api'),
    ]
