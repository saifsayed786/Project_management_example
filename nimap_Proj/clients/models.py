from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by =models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.client_name

class Project(models.Model):
    project_name=models.CharField(max_length=150)
    client_name=models.ForeignKey(Client,on_delete=models.CASCADE,related_name = 'clientproject')
    created_at = models.DateTimeField(auto_now_add=True)
    createdBy = models.ForeignKey(User,on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.project_name