from random import random

from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Matches(models.Model):
    title = models.CharField('Название матча', max_length=100)
    photo = models.ImageField('Фото')
    price = models.CharField('Цена билета', max_length=40)
    numb_tickets = models.IntegerField('Кол-во билетов', default=0)
    date = models.DateTimeField('Дата')
    slug = models.SlugField(default='slug')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'

    # def save(self, *args, **kwargs):
    #     super(Matches, self).save(*args, **kwargs)
    #
    #     for p in range(1, 21):
    #         self.tickets.set(Tickets.objects.bulk_create(
    #             [Tickets(number=self.slug + str(p))]))

#
# def generation(sender, instance, created, **kwargs):
#     if created:
#         return None
#     for p in range(instance.numb_tickets):
#         instance.tickets.set(Tickets.objects.bulk_create(
#             [Tickets(number=instance.slug + str(p))]))
#
#
# post_save.connect(generation, sender=Matches)


class Tickets(models.Model):
    match = models.ForeignKey('Matches', on_delete=models.CASCADE, related_name='tickets', null=True)
    number = models.CharField('Номер билета', max_length=400, blank=True, primary_key=True)

   #
   # headline = models.CharField('Матч:')
   # buyer = models.
   #  self.tickets.set(Ticket.objects.bulk_create(
   #      [Ticket(place=place, row=row) for row in range(len(rows)) for place in range(len(places))])


    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'


class Teams(models.Model):
    name = models.CharField('Название команды', max_length=100)
    short_name = models.CharField('Короткое название', max_length=20)
    photo = models.ImageField('Фото')
    bio = models.TextField('Информация о команде', blank=True)
    coach = models.CharField('Тренер', max_length=100, blank=True)
    president = models.CharField('Президент', max_length=100, blank=True)
    year = models.IntegerField('Год основания', default=0, blank=True)
    off_link = models.CharField('Ссылка на офф сайт', max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    fav_team = models.OneToOneField('Teams', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return 'Данные о пользователе {}'.format(self.user.username)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'