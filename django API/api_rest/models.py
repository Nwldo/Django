from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f'Nome: {self.name} | E-mail: {self.email} | Anos: {self.age}'