import uuid
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
LanguageChoices = (
    ('c', 'c'),
    ('cpp' , 'cpp'),
    ('csharp', 'csharp'),
    ('java' , 'java'),
    ('python' , 'python'),
   )


class MyCodes(models.Model):
    id  =  models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.TextField(null=False)
    title = models.CharField(max_length=100 , null = False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    language = models.CharField(max_length=20,choices=LanguageChoices, default=None )

    def __str__(self):
        return self.title
    
class Consumer(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE)
    name = models. CharField(max_length=200)
    avatar  =  models.ImageField ( upload_to='avatar' , blank =  True, null = True)


    def __str__(self):
        return self.name

  