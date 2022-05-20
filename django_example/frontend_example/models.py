from django.db import models


class GEOPointCharacteristic(models.Model):
    ts = models.DateTimeField(
        verbose_name='Момент замера',
        help_text='time stamp of measurement',
    )
    lat = models.FloatField(
        verbose_name='Широта',
        help_text='latitude',
    )
    lng = models.FloatField(
        verbose_name='Долгота',
        help_text='longitude',
    )
    co2 = models.FloatField(
        verbose_name='Уровень CO2 в воздухе',
    )

    def __str__(self):
        return f'GEOPoint([{self.ts}] ({self.lat};{self.lng}) CO2={self.co2}ppm)'
