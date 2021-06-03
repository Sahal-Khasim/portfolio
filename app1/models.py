from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=300, default='name')
    email = models.CharField(max_length=30, default='mail@mail.com')
    message = models.CharField(max_length=40, default='message me')
    def __str__(self):
        template = '{0.name} {0.email} {0.message}'
        return template.format(self)
