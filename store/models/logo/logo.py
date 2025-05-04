from django.db import models


class Logo(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='uploads/logo')

    def __str__(self):
        return self.name

    @staticmethod
    def get_logo():
        return Logo.objects.all()
