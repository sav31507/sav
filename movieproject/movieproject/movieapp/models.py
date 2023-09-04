from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class movie(models.Model):
    name=models.CharField(max_length=150)
    year=models.IntegerField()
    des=models.CharField(max_length=150)
    image=models.ImageField(upload_to='IMAGE')

    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width = "100"/>')


# refer note