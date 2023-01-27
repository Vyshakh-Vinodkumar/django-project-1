from django.db import models

# Create your models here.  
class Feedback(models.Model):
    name=models.CharField((""), max_length=50)
    email=models.CharField((""), max_length=50)
    phoneno=models.CharField((""), max_length=50)
    desc=models.CharField((""), max_length=500)
    # date=models.DateField((""), auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.name