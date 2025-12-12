from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Place(models.Model):
    PLACE_TYPES = [
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кафе'),
        ('bar', 'Бар'),
        ('park', 'Парк'),
        ('cinema', 'Кінотеатр'),
        ('club', 'Клуб'),
        ('other', 'Інше'),
    ]

    name = models.CharField(max_length=200, verbose_name="Назва")
    description = models.TextField(verbose_name="Опис")
    place_type = models.CharField(max_length=20, choices=PLACE_TYPES, verbose_name="Тип місця")
    location = models.CharField(max_length=200, blank=True, verbose_name="Локація")
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name="Рейтинг"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        verbose_name = "Місце"
        verbose_name_plural = "Місця"
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_preview_description(self, words=10):

        words_list = self.description.split()
        if len(words_list) <= words:
            return self.description
        return ' '.join(words_list[:words]) + '...'
