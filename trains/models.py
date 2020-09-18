from django.db import models

from cities.models import City


class Train(models.Model):
    name = models.CharField(max_length=180, unique=True, verbose_name='Номер поїзда')
    from_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Звідки', related_name='from_city')
    to_city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Куди', related_name='to_city')
    travel_time = models.IntegerField(verbose_name='Час у дорозі')

    class Meta:
        verbose_name = 'Поїзд'
        verbose_name_plural = 'Поїзда'
        ordering = ['name']

    def __str__(self):
        return f'{self.name} з м.{self.from_city} в м.{self.to_city}'