from django.db import models


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


class User(models.Model):
    first_name = models.CharField(verbose_name='Имя', help_text='Введите имя пользователя', max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(verbose_name='Ник', max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    age = models.PositiveIntegerField()
    location_id = models.ManyToManyField(Location)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=60, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Ad(models.Model):
    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null=True)
    price = models.PositiveIntegerField()
    description = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(upload_to='pictures', blank=True, null=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='ads')

    def __str__(self):
        return self.name
