from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from samplecloud.backend.models import Sampleset, Profile
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import schemas
from samplecloud.backend import serializers


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializer_class = serializers.UserSerializer


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()

    serializer_class = serializers.ProfileSerializer


@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def schema_view(request):

    generator = schemas.SchemaGenerator(title='SampleCloud API')

    return Response(generator.get_schema(request=request))
