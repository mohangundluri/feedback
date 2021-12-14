from django.db import models

#class Back(models.Model):
#    username = models.CharField(max_length=20)
#    email = models.EmailField(null=False,blank=True)
#    password = models.CharField(max_length=20)
    
class Back1(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(null=False,blank=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} {self.email} {self.password}"
