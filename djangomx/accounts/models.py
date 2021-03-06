# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

from sorl.thumbnail import ImageField
from django_gravatar.helpers import get_gravatar_url


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    _avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    cover = ImageField(upload_to='covers', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return u'{}'.format(self.user.username)

    @property
    def avatar(self):
        return self._avatar

    @avatar.setter
    def avatar(self, value):
        self._avatar = get_gravatar_url(value)

    @classmethod
    def create_from_user(cls, user, **kwargs):
        """ Creates and saves a Profile with given User. """
        obj = cls(**kwargs)
        obj.user = user
        obj.avatar = user.email
        obj.save()
        return obj
