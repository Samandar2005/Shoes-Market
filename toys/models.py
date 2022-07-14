from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ["-name"]

    def __str__(self) -> str:
        return f"{self.name}"


class Company(models.Model):
    title = models.CharField(max_length=50)
    workers = models.FloatField()
    annual_income = models.FloatField()
    email = models.EmailField()

    def __str__(self) -> str:
        return f"{self.title} {self.workers} {self.annual_income} {self.email}"


class Compound(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.name}"


class Material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"


class Shoes(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    company = models.ForeignKey(Company,  on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    the_size = models.FloatField()
    material = models.ManyToManyField('Material')
    сompound = models.ForeignKey(Compound, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='static/images')
    price = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def save(self) -> None:
        return super().save()

    def __str__(self) -> str:
        return f"{self.name} {self.brand} {self.company}{self.color} {self.the_size} {self.material} {self.сompound}  {self.img}  {self.price} {self.date} "


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shoes = models.ForeignKey(Shoes, on_delete=models.DO_NOTHING)
