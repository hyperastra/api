from django.conf.urls import url
from django.urls import path

from auth import views

urlpatterns = [
    url(r"^sign_up/$", views.SignUpView.as_view(), name="sign-up"),
    path("verify", views.VerifyView.as_view(), name="verify-user-account"),
    path("signed", views.VerifyView.as_view(), name="user-last-login"),
]
