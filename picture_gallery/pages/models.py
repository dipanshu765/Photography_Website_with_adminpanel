from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=20)
    category = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='content/image')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=20)
    image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name + " - " + self.category


class Team(models.Model):
    member_name = models.CharField(max_length=20)
    profile_image = models.ImageField(upload_to='team/profile')
    post = models.CharField(max_length=30)
    facebook_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)

    def __str__(self):
        return self.member_name+" - "+self.post

