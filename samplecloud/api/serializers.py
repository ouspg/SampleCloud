from rest_framework import serializers
from django.contrib.auth.models import User
from samplecloud.api.models import Sampleset, SamplesetVersion


class UserSerializer(serializers.HyperlinkedModelSerializer):

    samplesets = serializers.HyperlinkedIdentityField(view_name="sampleset-details", many=True)

    class Meta:

        model = User
        fields = ('url', 'id','username', 'email', 'first_name', 'last_name', 'password', 'samplesets')
        extra_kwargs = {'password': {'write_only': True}}


class SamplesetSerializer(serializers.HyperlinkedModelSerializer):

    versions = serializers.HyperlinkedIdentityField(view_name="samplesetversion-details", many=True)

    class Meta:

        model = Sampleset
        fields = ('url', 'id', 'name', 'author', 'versions')

class SamplesetVersionSerializer(serializers.HyperlinkedModelSerializer):

    sampleset = serializers.ReadOnlyField(source="sampleset.name")

    class Meta:

        model = SamplesetVersion
        fields = ('url', 'id', 'version', 'sampleset', 'file')
