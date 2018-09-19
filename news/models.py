from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from tastypie.utils.timezone import now
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.TextField(max_length=500, blank=True)


class News(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        # For automatic slug generation.
        if not self.slug:
            self.slug = slugify(self.title)[:30]

        return super(News, self).save(*args, **kwargs)
