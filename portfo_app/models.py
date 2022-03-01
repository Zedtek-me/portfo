from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return self.name, self.surname


class Details(models.Model):
    visitor= models.ForeignKey(Visitor, on_delete= models.CASCADE)
    others= models.CharField(max_length=500)

    def __str__(self):
        return self.others