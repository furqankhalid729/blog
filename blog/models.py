from django.db import models
from django.db import models
from django.urls import reverse

# Create your models here.
class post(models.Model):
    Title=models.CharField(max_length=300)
    Author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    Body=models.TextField()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('detailview',args=[str(self.id)])
