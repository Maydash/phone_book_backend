from django.urls import path, re_path
from .filters import *
from .views import *

urlpatterns = [
    path('api/getphonebooklist', PhoneBookList.as_view(), name='phone-book-list-api'),
    path('api/getplaceofworklist', PlaceOfWorkList.as_view(), name='place-of-work-list-api'),
    path('api/getcomingbirthdays', get_coming_birthdays, name='get_coming_birthdays-api'),
    path('api/getbirthdaytoday', birthday_today, name='get_birthday_today-api'),
    path('api/getsearch', Search.as_view(), name='get_search-api'),#http://127.0.0.1:8000/api/getsearch?q=aman
    re_path(r'^api/phonebook/filter/$', FilterPhonebooks.as_view(), name='filtering-all-phonebook'),#api/phonebook/filter/?place_of_work=Ashgabat kazyyet
    ]

