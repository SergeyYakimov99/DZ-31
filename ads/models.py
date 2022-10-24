from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from dateutil.relativedelta import relativedelta
from datetime import date
from django.core.exceptions import ValidationError

USER_MIN_AGE = 9


def birth_date_validator(value):
    diff = relativedelta(date.today(), value)
    if diff < USER_MIN_AGE:
        raise ValidationError("Пользователь младше 9 лет")
    return value


class Location(models.Model):
    name = models.CharField(max_length=50)
    lat = models.CharField(max_length=20)
    lng = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class UserRoles:
    USER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = (
        ("Пользователь", USER),
        ("Админ", ADMIN),
        ("Модератор", MODERATOR),
    )


class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    age = models.PositiveIntegerField(null=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[birth_date_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=60, unique=True)
    slug = models.CharField(verbose_name="Слаг", max_length=10, unique=True, validators=[MinLengthValidator(5)])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    name = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='ads')

    def __str__(self):
        return self.name


class Selection(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selections')
    name = models.CharField(max_length=100, unique=True)
    items = models.ManyToManyField(Ad)

    class Meta:
        verbose_name = "Подборка объявлений"
        verbose_name_plural = "Подборки объявлений"

    def __str__(self):
        return self.name
