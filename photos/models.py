from django.db import models

# Create your models here.
class Photo(models.Model):
    class Meta:
        db_table = "photo"

    name = models.CharField(max_length=255, null=False)
    photo = models.FileField(upload_to ='uploads/', null=False)

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)