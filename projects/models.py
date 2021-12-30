from django.db import models
import uuid

# Create your models here.


class Projects(models.Model):
    title = models.CharField(max_length=200)
    featured_image = models.ImageField(
        blank=True, null=True, default='default.jpg')
    location = models.TextField(max_length=100,null=True, blank=True)
    owner_name = models.TextField(max_length=100,null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.title 

class Tag(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
