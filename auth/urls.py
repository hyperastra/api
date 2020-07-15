from django.conf.urls import url

from auth import views

urlpatterns = [
    url(r'^sign_up/$', views.SignUpView.as_view(), name='sign-up'),
]
