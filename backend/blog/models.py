from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify

class Categories(models.TextChoices):
    CALCULUS = 'calculus'
    LINEAR_ALGEBRA = 'linear algebra'

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    thumbnail = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    month = models.CharField(max_length = 10)
    day = models.CharField(max_length = 2)
    content = models.TextField()
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slug
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title