from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from users.models import User

NULLABLE = {"blank": True, "null": True}


class Direction(models.Model):
    """Модель направления"""

    name_direction = models.CharField(max_length=100, verbose_name="наименование")
    description = models.TextField(verbose_name="описание направления")

    def __str__(self):
        return f"{self.name_direction} {self.description}"

    class Meta:
        verbose_name = "Направление"
        verbose_name_plural = "Направления"


class Doctor(models.Model):
    """Модель доктора-специалиста"""

    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    photo = models.ImageField(upload_to="person/", verbose_name="фото", **NULLABLE)
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, verbose_name="направление", **NULLABLE
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "врач"
        verbose_name_plural = "врачи"


class Service(models.Model):
    """Модель услуги"""

    name_service = models.CharField(max_length=250, verbose_name="наименование")
    description = models.CharField(verbose_name="артикул", **NULLABLE)
    direction = models.ForeignKey(
        Direction, on_delete=models.CASCADE, verbose_name="направление"
    )
    price = models.IntegerField(verbose_name="стоимость")

    def __str__(self):
        return f"{self.name_service} {self.price}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    """Модель записи на диагностику"""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="записи",
        verbose_name="пациент",
        **NULLABLE,
    )
    service = models.ForeignKey(
        Service, on_delete=models.CASCADE, related_name="записи", verbose_name="услуга"
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="записи", verbose_name="врач"
    )
    date = models.DateTimeField(verbose_name="дата и время приема")

    def __str__(self):
        return f"{self.user}: {self.date} {self.service}, {self.doctor}"

    class Meta:
        verbose_name = "запись на диагностику"
        verbose_name_plural = "записи на диагностику"

    def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        now = timezone.now()
        if self.date < now:
            raise ValidationError("Нельзя создать запись в прошедшем времени")
