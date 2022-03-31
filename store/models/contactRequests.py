from django.db import models


class Contact_Request(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.EmailField(max_length=50, default="")
    phone = models.CharField(max_length=15, default="")
    message = models.CharField(max_length=122, default="")

    def __str__(self):
        return self.name
