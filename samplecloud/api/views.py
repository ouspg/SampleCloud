from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from samplecloud.api.models import Sampleset, SamplesetVersion
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import schemas
from samplecloud.api import serializers
from django.contrib.auth import get_user_model
from rest_framework.decorators import detail_route, list_route


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()

    serializer_class = serializers.UserSerializer

    @detail_route(methods=['GET', 'POST'])
    def profile(self, request):

        # TODO: user profile endpoint

        #user = self.get_object()

        #return Response(user.profile)
        pass


class SamplesetViewSet(viewsets.ModelViewSet):

    queryset = Sampleset.objects.all()

    serializer_class = serializers.SamplesetSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @detail_route(methods=['GET', 'POST', 'DELETE'])
    def versions(self, request):

        """
        Manage versions of the sampleset.
        """

        # TODO: sampleset versions endpoint
        pass


@api_view()
@renderer_classes([renderers.CoreJSONRenderer, renderers.BrowsableAPIRenderer])
def schema_view(request, format=None):

    generator = schemas.SchemaGenerator(title='SampleCloud API')

    return Response(generator.get_schema(request=request))
