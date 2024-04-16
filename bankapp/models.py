from django.db import models
# Create your models here.
class District(models.Model):
    name=models.CharField(max_length=40)
    class Meta:
        db_table='District'

    def __str__(self):
        return '{}'.format(self.name)
class City(models.Model):
    district=models.ForeignKey(District, on_delete=models.CASCADE)
    name=models.CharField(max_length=40)
    class Meta:
        db_table='City'

    def __str__(self):
        return '{}'.format(self.name)
class Branch1(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=250)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email=models.CharField(max_length=100)
    address=models.TextField()
    district=models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)
    city=models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    account_type=models.CharField(max_length=250)
    material_provide=models.CharField(max_length=250)
    class Meta:
        db_table='Branch1'

    def __str__(self):
        return '{}'.format(self.last_name)
