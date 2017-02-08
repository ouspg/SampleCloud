from rest_framework import serializers
from django.contrib.auth import get_user_model
from samplecloud.api.models import Sampleset, SamplesetVersion


class UserSerializer(serializers.HyperlinkedModelSerializer):

    samplesets = serializers.HyperlinkedRelatedField(view_name="sampleset-details", many=True, read_only=True)

    class Meta:

        model = get_user_model()
        fields = ('url', 'id','username', 'email', 'first_name', 'last_name', 'password', 'samplesets')
        extra_kwargs = {'password': {'write_only': True}}


class SamplesetSerializer(serializers.HyperlinkedModelSerializer):

    versions = serializers.HyperlinkedRelatedField(view_name="sampleset-version-detail", many=True, read_only=True)

    class Meta:

        model = Sampleset
        fields = ('url', 'id', 'name', 'author', 'versions')

class SamplesetVersionSerializer(serializers.HyperlinkedModelSerializer):

    sampleset = serializers.HyperlinkedRelatedField(view_name="sampleset-details", read_only=True)

    class Meta:

        model = SamplesetVersion
        fields = ('url', 'id', 'version', 'sampleset', 'file')
