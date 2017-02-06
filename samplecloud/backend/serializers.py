from rest_framework import serializers
from django.contrib.auth.models import User, Group
from samplecloud.backend.models import Sampleset, Profile


class UserSerializer(serializers.Serializer):

    class Meta:

        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = ('__all__')


class SamplesetSerializer(serializers.ModelSerializer):

    class Meta:

        model = Sampleset
        fields = ('__all__')
