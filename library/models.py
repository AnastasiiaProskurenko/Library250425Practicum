from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Имя автора", help_text="Author's name")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия автора", help_text="Author's lastname")
    birthday = models.DateField(verbose_name="Дата рождения автора", help_text="Author's birthday")
    profile =  models.URLField(blank=True, null=True, verbose_name="Профиль автора", help_text="Author's linkprofile")
    deleted = models.BooleanField(default=False, verbose_name="Удален ли автор", help_text="deleted or not author's profile")
    rating = models.FloatField(verbose_name="Рейтинг автора", help_text="Author's raiting",
        validators=[MinValueValidator(0),
                    MaxValueValidator(10)],
        default=0
    )

    def __str__(self):
        return f"{self.last_name[0]}.{self.first_name}"
