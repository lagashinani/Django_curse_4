import csv
import datetime


from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as csvfile:

            phone_reader = csv.reader(csvfile, delimiter=';')
            # пропускаем заголовок
            next(phone_reader)

            for line in phone_reader:
                Phone.objects.create(id=int(line[0]),
                                     name=line[1],
                                     image=line[2],
                                     price=float(line[3]),
                                     release_date=datetime.datetime.strptime(line[4], '%Y-%m-%d'),
                                     lte_exists=True if line[5] == 'True' else False,
                                     slug=slugify(line[1]))
