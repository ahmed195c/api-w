from django.db import models

# Create your models here.

class User(models.Model):
    userName =  models.TextField(max_length=40)
    userEmail = models.TextField(max_length=50)


    def serilize(self):
        return{
            "name": self.userName,
            "email": self.userEmail
        }