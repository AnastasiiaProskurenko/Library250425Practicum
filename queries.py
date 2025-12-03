import os

import django



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from  library.models.author import Author
from datetime import date

# ## Задача 5: Поиск авторов с использованием field lookups
# **ТЗ:**
# 1. Найти всех авторов, чье имя начинается с 'A'
# 2. Найти авторов с рейтингом выше 8.5
# 3. Найти авторов, родившихся после 1950 года
# 4. Получить первого автора из результата

# authors = Author.objects.filter(first_name__startswith="A")
#
# authors_rating = Author.objects.filter(rating__gt=8.5)
#
# #authors_b_day = Author.objects.filter(birthday__gt="1950-01-01")
#
# authors_b_day = Author.objects.filter(birthday__gt=date(1950, 1, 1))
#
# first_b_author = authors_b_day.first()
#
# print("1 ", authors)
# print("2 ", authors_rating)
# print("3 ", authors_b_day)
# print("4 ", first_b_author)
#
#
# ## Задача 8: Массовое обновление членов библиотеки
# **ТЗ:**
# 1. Найти всех членов библиотеки с ролью 'lib_member'
# 2. Массово обновить их статус active на True
# 3. Использовать bulk_update для оптимизации

from library.models import Member
from library.enums import Role

moderators = Member.objects.filter(role=Role.moderator.name)
for moderator in moderators:
    moderator.active = False

Member.objects.bulk_update(moderators, ['active'])

print(f"Обновлено {moderators.count()} модераторов")

## Задача 12: Поиск просроченных займов с использованием Q объектов
# **ТЗ:**
# 1. Найти все займы (Borrow), которые не возвращены (returned=False)
# 2. Среди них найти те, где return_date уже прошла (меньше текущей даты)
# 3. Исключить займы, где return_date равно None
# 4. Отсортировать по дате займа (старые первыми)
from library.models import Borrow
from django.utils import timezone
from django.db.models import Q
today = timezone.now().date()

data = Borrow.objects.filter(
    Q(returned=False) &
    Q(Q(return_date__lt=today) |
    Q(return_date__isnull=True))
    ).order_by('borrow_date')

print(f"Найдено просроченных займов: {data.count()}")

for item in data[:20]:
    print(item.returned, item.return_date, item.actual_return_date)