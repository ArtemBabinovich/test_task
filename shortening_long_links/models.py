import random
import string

from django.contrib.auth.models import User
from django.db import models

from configuration.settings import ALLOWED_HOSTS


class Links(models.Model):
    """Base links"""
    user = models.ForeignKey(User, related_name='link', on_delete=models.CASCADE)
    links = models.URLField('links', max_length=250)
    slug = models.URLField('short_links', max_length=50, unique=True, blank=True)

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'

    def __str__(self):
        return self.links

    def __unicode__(self):
        return '%s  %s' % (self.links, self.slug)

    def save(self, *args, **kwargs):
        length = 6
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase
        short_id = ''.join(random.choice(char) for _ in range(length))
        short = ALLOWED_HOSTS[0]
        self.slug = short + '/' + short_id
        super(Links, self).save(*args, **kwargs)
