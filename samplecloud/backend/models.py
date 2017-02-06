from django.db import models
from django.contrib.auth.models import User, Group


class Profile(models.Model):

    """
    Profile class to compliment the User class.
    Includes profile info and settings.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40)
    bio = models.CharField(max_length=500)


class Project(models.Model):

    """
    Project class to compliment the Group class.
    Includes project information and settings.
    """

    group = models.OneToOneField(Group)
    members = models.ManyToManyField(User)
    bio = models.CharField(max_length=500)


class Sampleset(models.Model):

    """
    Class for identifying a sampleset.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, null=True)
    name = models.CharField(max_length=40)


class SamplesetVersion(models.Model):

    """
    Class for storing a single uploaded version of a sampleset.
    """

    sampleset = models.ForeignKey(Sampleset, on_delete=models.CASCADE)
    version = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="samples/{}/".format(sampleset.name))


class SamplesetCollection(models.Model):

    """
    Collection of samplesets.
    Useful for grouping relevant samplesets together (ex. by topic) for easier viewing and sharing.
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    samplesets = models.ManyToManyField(Sampleset)
