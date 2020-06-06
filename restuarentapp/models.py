from django.db import models
#from mongoengine import Document, EmbeddedDocument, fields
# Create your models here.


class Restuarent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    cuisines = models.CharField(max_length=100)
    cost = models.IntegerField()
    currency = models.CharField(max_length=20)
    booking = models.CharField(max_length=3, choices=[
        ('Yes','Yes'),
        ('No','No')]
                                     )
    delivery = models.CharField(max_length=3, choices=[
        ('Yes', 'Yes'),
        ('No', 'No')],
                                       )
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    colour = models.CharField(max_length=20, choices=[
        ('Dark Green','Dark Green'),
        ('Green','Green'),
        ('Orange','Orange'),
        ('Yellow','Yellow'),
        ('White','White')]
                                     )
    text = models.CharField(max_length=20, choices=[
        ('Excellent','Excellent'),
        ('Very Good','Very Good'),
        ('Good','Good'),
        ('Average','Average'),
        ('Not rated','Not rated')]
                                   )
    votes = models.CharField(max_length=10)

    def __str__(self):
        return self.name

