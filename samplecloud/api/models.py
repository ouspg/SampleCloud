from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings

class User(AbstractUser):

    """
    Custom User class for possible future exetensios.
    """

    pass


class UserProfile(models.Model):

    """
    Profile class to compliment the User class.
    Includes profile info and settings.
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    bio = models.CharField(max_length=500)


class Project(models.Model):

    """
    Project class to compliment the Group class.
    Includes project information and settings.
    """

    group = models.OneToOneField(Group)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL)
    bio = models.CharField(max_length=500)


class Sampleset(models.Model):

    """
    Class for identifying a sampleset.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='samplesets', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True)
    name = models.CharField(max_length=40, unique=True)


class SamplesetVersion(models.Model):

    """
    Class for storing a single uploaded version of a sampleset.
    """

    sampleset = models.ForeignKey(Sampleset, related_name="versions", on_delete=models.CASCADE)
    version = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="samples/{}/".format(sampleset.name))


class SamplesetCollection(models.Model):

    """
    Collection of samplesets.
    Useful for grouping relevant samplesets together (ex. by topic) for easier viewing and sharing.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    samplesets = models.ManyToManyField(Sampleset)
