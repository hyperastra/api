from auth import views
from django.conf.urls import url

urlpatterns = [
    url(r'^signup/$', views.SignUpView.as_view(), name='sign-up'),
]
