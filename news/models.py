from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone
from tastypie.utils.timezone import now
from django.utils.text import slugify
from django.db.utils import IntegrityError


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return str(self.user.first_name) + ' ' + str(self.user.last_name)


class News(models.Model):
    writer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.title) + ' by ' + str(self.writer.user.username)

    def save(self, *args, **kwargs):
        # To autogenerate a slug and ensure valid/unique slugs
        if not self.slug:
            new_slug = slugify(self.title[:30])
            valid_slug = new_slug
            counter = 1
            while News.objects.filter(slug=valid_slug).exists():
                valid_slug = new_slug + '-' + str(counter)
                counter += 1
            self.slug = valid_slug
        return super(News, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-pub_date"]
