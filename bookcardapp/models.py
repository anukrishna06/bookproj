from django.db import models

# Create your models here.
class books(models.Model):
    bookid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=220)
    author = models.CharField(max_length=220)
    image = models.ImageField(upload_to='image',null=True)
    description = models.TextField(null=True)

    class Meta:
        db_table = "booktable"
