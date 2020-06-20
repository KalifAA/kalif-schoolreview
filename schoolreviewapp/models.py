from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from model_utils.models import TimeStampedModel

# Create your models here.
class School(models.Model):
    CATEGORIES = (
        (1, 'Elementary'),
        (2, 'Middleschool'),
        (3, 'Highschool'),
    )

    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    city = models.IntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    longitude = models.DecimalField(max_digits=10, decimal_places=2)
    public = models.BooleanField()
    students = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name

    @property
    def main_image(self):
        return self.images.first()


class SchoolImage(TimeStampedModel):
    image = models.ImageField(upload_to='schools')
    school = models.ForeignKey(School, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.school.name
    
class Comment(TimeStampedModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(blank=True, null=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.author

    def __str__(self):
        return self.text