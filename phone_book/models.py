from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class PlaceOfWork(MPTTModel):
    title = models.CharField(verbose_name='Edaranyň ady', max_length=100, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Edaranyň ady'
        verbose_name_plural = 'Edaranyň atlary'


class Location(models.Model):
    title = models.CharField(verbose_name='Ýerleşýän ýeri(Şäher, etrap)', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ýerleşýän ýeri(Şäher, etrap)'
        verbose_name_plural = 'Ýerleşýän ýerleri(Şäher, etrap)'


class DepartmentName(models.Model):
    title = models.CharField(verbose_name='Bolümiň ady', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Bolümiň ady'
        verbose_name_plural = 'Bolümiň atlary'


class Position(models.Model):
    title = models.CharField(verbose_name='Wezipesi', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Wezipesi'
        verbose_name_plural = 'Wezipeleri'


class PhoneBook(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Ady')
    last_name = models.CharField(max_length=50, verbose_name='Familiyasy')
    place_of_work = models.ForeignKey(
        PlaceOfWork, on_delete=models.SET_NULL, null=True, verbose_name='Isleyan yeri', related_name='place_of_work'
    )
    department_name = models.ForeignKey(
        DepartmentName, on_delete=models.SET_NULL, null=True, verbose_name='Bölümiň ady', related_name='department_name'
    )
    position = models.ForeignKey(
        Position, on_delete=models.SET_NULL, null=True, verbose_name='Wezipesi', related_name='position'
    )
    location = models.ForeignKey(
        Location, on_delete=models.SET_NULL, null=True, verbose_name='Ýerleşýän ýeri(Şäher, etrap)', related_name='location'
    )
    mobile_phone = models.CharField(max_length=50, verbose_name='El telefony')
    work_phone = models.CharField(max_length=50, verbose_name='Is telefony')
    home_address = models.CharField(max_length=250, verbose_name='Öý salgysy')
    birthday = models.DateField(verbose_name='Doglan guni')
