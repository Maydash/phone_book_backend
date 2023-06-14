from django.urls import path
from .views import *

urlpatterns = [
    path('api/getphonebooklist', PhoneBookList.as_view(), name='phone-book-list-api'),
    path('api/getcomingbirthdays', get_coming_birthdays, name='get_coming_birthdays-api'),
    path('api/getbirthdaytoday', birthday_today, name='get_birthday_today-api'),
    ]
