from django.db import models

# Create your models here.
class Careers_hub(models.Model):
    company_name=models.CharField(max_length=50)
    company_link=models.TextField(max_length=100)
    def __str__(self):
        return self.company_name


