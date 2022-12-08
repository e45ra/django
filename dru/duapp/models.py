from django.db import models
from django.forms import MultipleChoiceField
from django.core.validators import MaxValueValidator, MinValueValidator

class Drug(models.Model):
    name = models.CharField(max_length=30)
    gtn = models.IntegerField()
    lot = models.IntegerField()
    generic_name = models.CharField(max_length=50)
    Date_exp = models.IntegerField()
    
    def __str__(self):
        return '{}-{}'.format(self.pk, self.name)

class Store(models.Model):
    drugs = models.ForeignKey(Drug, on_delete=models.CASCADE, default=1)
    submit_date = models.IntegerField()
    price_main = models.IntegerField()
    amount = models.IntegerField()
    store_number = models.IntegerField()

    def __str__(self):
        return '{}-{}'.format(self.pk, self.drugs)


class Stores(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=50)

    def __str__(self):
        return '{}-{}'.format(self.pk, self.name)

    
class Cage(models.Model):
    drugs = models.ForeignKey(Drug, on_delete=models.CASCADE, default=0)
    submit_date = models.IntegerField()
    price_main = models.IntegerField()
    amount = models.IntegerField()
    cage_number = models.IntegerField()
    
    def __str__(self):
        return '{}-{}'.format(self.pk, self.drugs)

    
class PersonData(models.Model):
    name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    date = models.IntegerField()
    
    amar_afrad = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    modiriat_ghafase = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    ersal_payam = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    sabt_daro =  models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    sabt_noskhe = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    view_noskhe = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    jam_kardn_daro = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    view_daro = models.IntegerField(default=0, validators=[MaxValueValidator(1), MinValueValidator(0)])
    
    phone_number = models.IntegerField()
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return '{}-{}'.format(self.pk, self.name)
