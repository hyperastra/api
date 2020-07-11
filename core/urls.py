from django.conf.urls import include, url
from rest_framework_nested import routers


router = routers.SimpleRouter()


urlpatterns = [url(r"^", include(router.urls))]