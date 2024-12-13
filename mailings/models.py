from django.conf import settings
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

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    title = models.CharField(max_length=150, verbose_name='тема письма')
    text = models.TextField(verbose_name='текст письма')
    message_owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь',
                                      on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Clients(models.Model):
    client_email = models.EmailField(unique=True, verbose_name='email клиента')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    comments = models.TextField(verbose_name='комментарии', **NULLABLE)
    client_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                                     **NULLABLE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Mailings(models.Model):
    mailing_name = models.CharField(max_length=150, verbose_name='название рассылки', default=None)
    mailing_start = models.DateTimeField(verbose_name='дата и время начала рассылки', default=None)
    mailing_finish = models.DateTimeField(verbose_name='дата и время окончания рассылки', default=None)
    next_try = models.DateTimeField(verbose_name='дата и время следующей попытки', **NULLABLE)
    period = models.CharField(max_length=15, choices=PERIOD_CHOICES, verbose_name='периодичность')
    mailing_status = models.CharField(max_length=15, default='Создана', choices=STATUS_CHOICES, verbose_name='статус рассылки')
    client_email = models.ManyToManyField(Clients, verbose_name='контактный email')
    mailing_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='пользователь',
                                      **NULLABLE)
    mail_title = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='тема рассылки',
                                   default=None)
    is_active = models.BooleanField(default=True, verbose_name='активность рассылки')

    def __str__(self):
        return self.mailing_name

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    last_try = models.DateTimeField(auto_now=False, auto_now_add=False,
                                    verbose_name='дата и время последней попытки')
    status_try = models.CharField(max_length=20, verbose_name='статус попытки')
    server_answer = models.TextField(verbose_name='ответ сервера', **NULLABLE, default='')
    send_name = models.CharField(max_length=200, verbose_name='наименование рассылки',
                                 default=None)
    logs_owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='пользователь',
                                   on_delete=models.SET_NULL, **NULLABLE)
    send_email = models.EmailField(max_length=150, verbose_name='почта отправки', **NULLABLE)

    def __str__(self):
        return f"{self.status_try}: {self.last_try}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('-last_try',)
