from django.db import models

STATUS_CHOICES = (
    ('Завершена', 'Завершена'),
    ('Запущена', 'Запущена'),
    ('Создана', 'Создана'),
)

PERIOD_CHOICES = (
    ('Ежедневно', 'Ежедневно'),
    ('Еженедельно', 'Еженедельно'),
    ('Ежемесячно', 'Ежемесячно'),
)


class Clients(models.Model):
    email = models.EmailField(unique=True, verbose_name='email клиента')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comments = models.TextField(verbose_name='комментарии')


class MailingsSettings(models.Model):
    datatime = models.DateTimeField(auto_now_add=True, verbose_name='дата и время отправки рассылки')
    period = models.CharField(max_length=, default='создана', choices=PERIOD_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=15, default='создана', choices=STATUS_CHOICES, verbose_name='статус рассылки')


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')
