from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True, verbose_name="роль пользователя")

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        db_table = "custom_user_table"
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователь'


class Role(models.Model):
    TYPE_ROLE = (
        ('mentor', 'ментор'),
        ('manager', 'менеджер'),
        ('administrator', 'администратор'),
    )
    name = models.CharField(choices=TYPE_ROLE, max_length=15, unique=True, null=True, verbose_name='роль пользователя',
                            default='manager')

    class Meta:
        verbose_name_plural = 'роли'
        verbose_name = 'роль'

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=124, verbose_name='вид рекламы', unique=True)
    description = models.CharField(max_length=350, verbose_name='описание', null=True)
    slug = models.SlugField(verbose_name="URL", unique=True)
    date_created = models.DateTimeField(default=now, verbose_name="дата создания")
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'клиенты'
        verbose_name = 'клиент'


class Commercial_offer(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name='пользователь', on_delete=models.CASCADE)
    description = models.TextField(verbose_name="описание")
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость', default=0)
    number = models.PositiveSmallIntegerField(verbose_name='номер предложения', default=0)
    slug = models.SlugField(verbose_name="URL", unique=True)
    date_created = models.DateTimeField(default=now, verbose_name="дата создания")
    client = models.ForeignKey('Client', verbose_name='клиент', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'коммерческие предложения'
        verbose_name = 'коммерческое предложение'


class Advertising(models.Model):
    title = models.CharField(max_length=64, verbose_name='вид рекламы', unique=True)
    description = models.TextField(verbose_name="описание")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='стоимость', default=0)
    slug = models.SlugField(verbose_name="URL", unique=True)
    image = models.ImageField(upload_to='advertising_photos', verbose_name='картинка', null=True, blank=True)
    category = models.ForeignKey('AdvertisingCategory', verbose_name='категория', on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'виды рекламы'
        verbose_name = 'вид рекламы'

    def __str__(self):
        return self.title


class AdvertisingCategory(models.Model):
    name = models.CharField(max_length=64, verbose_name='категория')

    class Meta:
        verbose_name_plural = 'категрии рекламы'
        verbose_name = 'категрия рекламы'

    def __str__(self):
        return self.name
