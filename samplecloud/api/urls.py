from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from samplecloud.api import views
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
import rest_framework.urls


router = DefaultRouter(trailing_slash=False)

router.register(r'users', views.UserViewSet)
router.register(r'samples/sets', views.SamplesetViewSet)

urlpatterns = format_suffix_patterns([
    url(r'^schema$', views.schema_view),
], allowed=['json', 'corejson', 'api'])

urlpatterns += (url(r'', include(router.urls)),)

#urlpatterns += (url(r'admin/', include(rest_framework.urls)),)


# If drfdocs is in installed apps and debugging is enabled, add urls for api documentation

if "rest_framework_docs" in settings.INSTALLED_APPS and settings.DEBUG:

    urlpatterns += [url(r'docs/', include("rest_framework_docs.urls"))]
