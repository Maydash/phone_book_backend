from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import *
from .models import *
import django_filters


class FilterPhonebook(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    phone_number = django_filters.CharFilter(lookup_expr='icontains')
    place_of_work = django_filters.CharFilter(field_name='place_of_work__title')

    class Meta:
        model = PhoneBook
        fields = [
            'first_name',
            'last_name',
            'phone_number',
            'home_address',
            'place_of_work',
            'department_name',
            'position',
            'location',
        ]


class FilterPhonebooks(APIView):
    def get(self, request):
        queryset = PhoneBook.objects.all()
        filterset = FilterPhonebook(request.GET, queryset=queryset)
        if filterset.is_valid():
            queryset = filterset.qs
        serializer = PhoneBookSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

