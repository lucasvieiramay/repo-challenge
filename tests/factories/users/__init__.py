import factory
import random
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    full_name = factory.Faker("name")
    email = factory.LazyAttribute(lambda obj: '%s@triven.com' % obj.social_security_number)
