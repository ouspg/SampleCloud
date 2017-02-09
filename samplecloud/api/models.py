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

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name="profile",
                                on_delete=models.CASCADE)

    nickname = models.CharField(max_length=20)

    bio = models.CharField(max_length=500)


class Project(models.Model):

    """
    Project class to compliment the Group class.
    Includes project information and settings.
    """


    name = models.CharField(max_length=20)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL)

    description = models.CharField(max_length=200)

class Sampleset(models.Model):

    """
    Class for identifying a sampleset.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='samplesets',
                               on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)

    name = models.CharField(max_length=20, unique=True)

    description = models.CharField(max_length=200)


class SamplesetVersion(models.Model):

    """
    Class for storing a single uploaded version of a sampleset.
    """

    sampleset = models.ForeignKey(Sampleset,
                                  related_name="versions",
                                  on_delete=models.CASCADE)

    version = models.CharField(max_length=40)

    created = models.DateTimeField(auto_now_add=True)

    file = models.FileField(upload_to="samples/{}/".format(sampleset.name))

    notes = models.CharField(max_length=200)


class SamplesetCollection(models.Model):

    """
    Collection of samplesets.
    Useful for grouping relevant samplesets together (ex. by topic) for easier viewing and sharing.
    """

    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name="author",
                               on_delete=models.CASCADE)

    name = models.CharField(max_length=40)

    samplesets = models.ManyToManyField(Sampleset)
