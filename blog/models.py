from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='blog')
    description = models.TextField()
    post_link = models.URLField(blank=True)

    def __str__(self):
        return self.title
    
