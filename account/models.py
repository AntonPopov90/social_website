from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

GENDER_CHOICES = [
    ['Берег', u"Берег"],
    ['Лодка', u"Лодка"],
]

REL_CHOICES = [
    ['Не определено', u"Не определено"],
    ['макушатник', u"макушатник"],
    ['спининг', u"спининг"],
    ['фидер', u"фидер"],
    ['поплавочка', u"поплавочка"],
    ['багрильщик', u"багрильщик"],
]

FISH_CHOICES = [
    ['Макуха', u"Макуха"],
    ['Флет метод', u"Флет метод"],
    ['Цоколь', u"Цоколь"],
    ['Блесна', u"Блесна"],
    ['Пикер', u"Пикер"],
    ['Универсал', u"Универсал"],
    ['резинка', u"резинка"],
]


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.FileField(verbose_name=u"Аватар", null=True, blank=True,default='karp.jpg')
    gender = models.CharField(max_length=15, verbose_name=u"Предпочитаемый вид ловли", choices=REL_CHOICES, default="нет",null=True)
    relationship = models.CharField(max_length=30, verbose_name=u"Cпециализация", choices=FISH_CHOICES,
                                    default="нет",null=True)
    karas = models.IntegerField(verbose_name='Количество пойманных карасей',blank=True,null=True,default=0)
    sazan = models.IntegerField(verbose_name='Количество пойманных сазанов',blank=True,null=True,default=0)
    lech = models.IntegerField(verbose_name='Количество пойманных лещей',blank=True,null=True,default=0)
    other_fish = models.IntegerField(verbose_name='Прочая рыба',blank=True,null=True,default=0)
    fish_sum = models.PositiveIntegerField(verbose_name='Количество пойманной рыбы', blank=True, null=True)
    fish_kg = models.FloatField(max_length=25,verbose_name='Общий вес в кг', blank=True, null=True)
    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

class Sazan(models.Model):
    name = models.CharField(max_length=100, verbose_name='Cазан', choices=FISH_CHOICES, blank=True, null=True)
    sum = models.PositiveIntegerField(verbose_name='Количество рыбы', blank=True, null=True)
    kg = models.FloatField(verbose_name='Вес в кг', blank=True, null=True)


class Statistic(models.Model):
    place = models.CharField(max_length=100, verbose_name='Место',blank=True,null=True)
    date = models.DateField(verbose_name='Дата', blank=True, null=True)
    description = models.CharField(max_length=500, verbose_name='Краткое описание', blank=True, null=True,default='ноль')
    fish_name = models.CharField(max_length=500, verbose_name='Кого поймали', blank=True, null=True,default='ноль')
    fish_sum = models.PositiveIntegerField(verbose_name='Количество рыбы в шт.', blank=True, null=True,default=0)
    fish_kg = models.FloatField(verbose_name='Общий вес в кг', blank=True, null=True,default=0)
    vodka = models.FloatField(verbose_name='Количество распитой водочки,л', blank=True, null=True,default=0)
    beer = models.FloatField(verbose_name='Количество распитого пивка,л', blank=True, null=True,default=0)
    prikorm = models.FloatField(verbose_name='Количество прикорма,кг', blank=True, null=True,default=0)



class Trophy(models.Model):
    name = models.CharField(max_length=100, verbose_name='Место ловли', blank=True, null=True)
    description = models.CharField(max_length=500, verbose_name='Описание', blank=True, null=True)
    phase = models.FileField(upload_to='media/trophy',blank=False,null=False, default='/media/karp.jpg')


class News(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title