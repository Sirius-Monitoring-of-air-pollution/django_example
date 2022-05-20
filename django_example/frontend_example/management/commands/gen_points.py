import random

import pytz as pytz
from django.core.management.base import BaseCommand
from django.utils.datetime_safe import datetime

from frontend_example.models import GEOPointCharacteristic

POINTS = 10000

CHUVSU = (56.145381, 47.224436)
GEO_SCATTER = 0.005

PPM_MIN = 300
PPM_SCATTER = 500


class Command(BaseCommand):
    def handle(self, *args, **options):
        GEOPointCharacteristic.objects.all().delete()
        points = list()
        for _ in range(POINTS):
            ts = datetime.now(tz=pytz.UTC)
            lat = GEO_SCATTER * random.uniform(-1, 1) + CHUVSU[0]
            lng = GEO_SCATTER * random.uniform(-1, 1) + CHUVSU[1]
            ppm = PPM_MIN + PPM_SCATTER * random.uniform(0, 1)
            points.append(GEOPointCharacteristic(
                ts=ts,
                lat=lat,
                lng=lng,
                co2=ppm,
            ))
        GEOPointCharacteristic.objects.bulk_create(points, batch_size=100)
