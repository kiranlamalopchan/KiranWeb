from django.db import models


class Section(models.Model):
    title = models.CharField(max_length=100, null=True)
    sub_title = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length=500, null=True)
    image = models.ImageField(upload_to='uploads/sectionsimg/')

    def __str__(self):
        return self.title

    @staticmethod
    def get_section_detail():
        return Section.objects.all()
