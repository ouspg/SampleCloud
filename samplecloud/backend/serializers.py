from rest_framework import serializers
from samplecloud.backend.models import Sampleset, Profile

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = Profile
        fields = ('__all__')

class SampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sampleset
        fields = ('__all__')