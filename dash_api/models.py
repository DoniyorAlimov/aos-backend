from django.db import models

# Create your models here.


class Equipment_Type(models.Model):
    type = models.CharField(max_length=55)


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    equipment_type = models.ForeignKey(
        Equipment_Type, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.name


class Aggreagation_Type(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name


class Aggregation(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    aggregation_type = models.ForeignKey(
        Aggreagation_Type, on_delete=models.PROTECT)
    value = models.DecimalField(max_digits=10, decimal_places=6)
    timestamp = models.DateTimeField()
