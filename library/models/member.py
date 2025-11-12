from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from library.enums import Gender, Role


class Member(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(unique=True, verbose_name="Email")
    gender = models.CharField(max_length=50, choices=Gender.choices(), null=True, blank=True, verbose_name="Пол")
    birth_date = models.DateField(verbose_name="Дата рождения")
    age = models.IntegerField(validators=[MinValueValidator(6), MaxValueValidator(120)], verbose_name="Возраст")
    role = models.CharField(max_length=20, choices=Role.choices(), default=Role.guest, verbose_name="Роль")
    active = models.BooleanField(default=True, verbose_name="Активен")
    libraries = models.ManyToManyField('Library', related_name='members', blank=True)

    class Meta:
        db_table = 'members'
        verbose_name = "Member"
        verbose_name_plural = "Members"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name[0]}. {self.first_name} ({self.email})"
