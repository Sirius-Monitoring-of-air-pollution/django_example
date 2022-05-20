import numpy as np
import pandas as pd

from django.core.management.base import BaseCommand

from frontend_example.models import GEOPointCharacteristic


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        points = GEOPointCharacteristic.objects.all()
        data = np.array([(p.ts, p.lat, p.lng, p.co2) for p in points])
        df = pd.DataFrame(data, columns=['Момент замера', 'Широта', 'Долгота', 'Уровень CO2 в воздухе'])
        df['Момент замера'] = df['Момент замера'].dt.tz_localize(None)
        writer = pd.ExcelWriter(options['path'], 'xlsxwriter')
        df.to_excel(writer)
        writer.save()
