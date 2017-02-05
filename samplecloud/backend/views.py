from django.shortcuts import render
from rest_framework import viewsets
from samplecloud.backend.models import Sampleset, Profile
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import schemas
from samplecloud.backend.serializers import SampleSerializer, ProfileSerializer

# Create your views here.


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@api_view()
@renderer_classes([renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='SampleCloud API')
    return Response(generator.get_schema(request=request))


