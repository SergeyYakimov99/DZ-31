import faker

import data as data
import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'test',
    last_name = 'testiev',
    username = 'johny_test',
    email = 'sergik@test.ru',
    password = '123',
    birth_date = factory.Faker('date_object')

    class Meta:
        model = 'ads.User'


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'


class AdFactory(factory.django.DjangoModelFactory):
    name = 'Ad'
    author = factory.SubFactory(UserFactory)
    price = 1

    class Meta:
        model = 'ads.Ad'

