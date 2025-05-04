from django.db import models


class MainCategory(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
