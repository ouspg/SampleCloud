from rest_framework import serializers
from django.contrib.auth import get_user_model
from samplecloud.api.models import Sampleset, SamplesetVersion


class UserSerializer(serializers.HyperlinkedModelSerializer):

    samplesets = serializers.HyperlinkedRelatedField(view_name="sampleset-details", many=True, read_only=True)

    class Meta:

        model = get_user_model()
        fields = ('url','username', 'email', 'first_name', 'last_name', 'password', 'samplesets')
        extra_kwargs = {'password': {'write_only': True}}


class SamplesetVersionSerializer(serializers.ModelSerializer):


    class Meta:

        model = SamplesetVersion
        fields = ('version', 'notes', 'created', 'file')


class SamplesetSerializer(serializers.HyperlinkedModelSerializer):

    versions = SamplesetVersionSerializer

    class Meta:

        model = Sampleset
        fields = ('url', 'name', 'description', 'author', 'versions')
        extra_kwargs = {'versions': {'read_only': True}}