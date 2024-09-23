
from django.urls import path
from django.contrib.auth import views as auth_view 
from .views import *
urlpatterns = [
    path("accounts/signup/", ConsumerRegistrationFormView.as_view(), name="signup"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name  = "LoginForm.html" ,
                                                        authentication_form  = LoginForm ),
                                                        name="login"),
    path("logout/", LogoutView, name="logout"),
    # path("setTitle/", setTitle, name="setTitle"),
    path("saveCode/", SaveCode, name="saveCode"),
]

