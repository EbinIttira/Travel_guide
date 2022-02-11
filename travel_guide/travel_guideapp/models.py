from django.db import models

class myplaces(models.Model):
    place=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    desc=models.TextField(max_length=700)
    img=models.ImageField(upload_to='pictures')

    def __str__(self):
        return self.name

