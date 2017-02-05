from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from samplecloud.backend import views
from django.conf import settings

app_name = "backend"

router = DefaultRouter(trailing_slash=False)

router.register(r'^profiles/', views.ProfileViewSet)

urlpatterns = [
    url(r'^schema$', views.schema_view),
    url(r'', include(router.urls)),
]


# If drfdocs is in installed apps, add urls for api documentation

if "rest_framework_docs" in settings.INSTALLED_APPS:

    urlpatterns += [url(r'docs/', include("rest_framework_docs.urls"))]