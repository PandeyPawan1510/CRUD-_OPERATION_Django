from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    class Meta:
        db_table="client"
    def __str__(self):
        return self.name
class Project(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField()
    month=models.DateField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)

    class Meta:
        db_table="project"






