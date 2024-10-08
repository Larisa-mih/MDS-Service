from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Создание суперпользователя"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mih.ru",
            first_name="admin",
            last_name="admin",
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        user.set_password("123qwer")
        user.save()
