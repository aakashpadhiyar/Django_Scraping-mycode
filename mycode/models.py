from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    Created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search[:20]

    class Meta:
        verbose_name_plural = 'Searches'
