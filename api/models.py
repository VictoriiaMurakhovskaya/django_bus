from django.db import models
import json


class Station(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} ({self.id})'


class Carrier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Interval(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.ManyToManyField(Station, max_length=40, related_name='%(class)s_starts')
    finish = models.ManyToManyField(Station, max_length=40, related_name='%(class)s_finishes')
    start_time = models.TimeField()
    finish_time = models.TimeField()
    cost = models.FloatField()


class Route(models.Model):
    id = models.IntegerField(primary_key=True)
    carrier = models.ForeignKey(Carrier, max_length=100, null=True, on_delete=models.SET_NULL)
    route_sequence = models.CharField(max_length=300)
    start = models.ManyToManyField(Station, max_length=40, related_name='%(class)s_starts')
    finish = models.ManyToManyField(Station, max_length=40, related_name='%(class)s_finishes')

    def set_sequence(self, value):
        self.route_sequence = json.dumps(value)

    def get_sequence(self):
        return json.loads(self.route_sequence)


class Carriage(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    route = models.ForeignKey(Route, max_length=4, on_delete=models.PROTECT)
    tickets = models.BinaryField()

    def __str__(self):
        return f'Дата: {self.date}: Маршрут: {self.route.id}'



