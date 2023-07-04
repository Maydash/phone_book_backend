from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from datetime import date, datetime
import datetime
from django.db.models import Q
from .serializers import *
from .models import *





class PhoneBookList(ListAPIView):
    queryset = PhoneBook.objects.all()
    serializer_class = PhoneBookSerializer


class PlaceOfWorkList(ListAPIView):
    queryset = PlaceOfWork.objects.all()
    serializer_class = PlaceOfWorkSerializer


#doglan gune 1 hepde galsa spisoga goshulyar
@api_view(['GET'])
def get_coming_birthdays(request):
    coming_birthdays = []
    today = datetime.date.today()
    start_of_year = datetime.date(today.year, 1, 1)
    #yylyn bashyndan bari shu gune cenli nace gun gecdi
    days_since_start = (today - start_of_year)
    for item in PhoneBook.objects.all():
        my_date = item.birthday
        days_passed = my_date - date(my_date.year, 1, 1)
        if 0 > (days_since_start - days_passed).days < 7:
            coming_birthdays.append(item)
    serializer = PhoneBookSerializer(coming_birthdays, context={'request': request}, many=True)
    return Response(serializer.data)


#shu gun doglan guni bolsa spisoga goshulyar
@api_view(['GET'])
def birthday_today(request):
    birthday_today = []
    today = datetime.date.today()
    start_of_year = datetime.date(today.year, 1, 1)
    #yylyn bashyndan bari shu gune cenli nace gun gecdi
    days_since_start = (today - start_of_year)
    for item in PhoneBook.objects.all():
        my_date = item.birthday
        days_passed = my_date - date(my_date.year, 1, 1)
        if my_date.year % 4 == 0 and (days_since_start.days + datetime.timedelta(days=1).days) == days_passed.days:
            birthday_today.append(item)
        if days_since_start.days == days_passed.days:
            birthday_today.append(item)
    serializer = PhoneBookSerializer(birthday_today, context={'request': request}, many=True)
    return Response(serializer.data)

class Search(ListAPIView):
    """Gozleg"""
    serializer_class = PhoneBookSerializer

    def get_queryset(self):
        return PhoneBook.objects.filter(
            Q(first_name__icontains=self.request.GET.get("q")) |
            Q(last_name__icontains=self.request.GET.get("q")) |
            Q(place_of_work__title__icontains=self.request.GET.get("q")) |
            Q(mobile_phone__icontains=self.request.GET.get("q")) |
            Q(work_phone__icontains=self.request.GET.get("q")) |
            Q(home_address__icontains=self.request.GET.get("q"))
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context

