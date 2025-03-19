from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """
    Кастомная модель пользователя, включающая в себя поле
    с номером телефона.
    """

    phone_number = models.CharField(
        "Номер телефона",
        max_length=12,
        null=True,
        blank=True,
    )
    mentor = models.ForeignKey(
        "self",
        verbose_name="Наставник",
        related_name="users",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
