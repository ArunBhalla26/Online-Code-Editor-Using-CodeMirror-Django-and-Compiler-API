
from django.urls import path
from django.contrib.auth import views as auth_view 
from .views import *
urlpatterns = [
    path("accounts/signup/", ConsumerRegistrationFormView.as_view(), name="signup"),
    path("accounts/login/", auth_view.LoginView.as_view(template_name  = "LoginForm.html" ,
                                                        authentication_form  = LoginForm ),
                                                        name="login"),
    path("logout/", LogoutView, name="logout"),
    path("saveCode/", SaveCode, name="saveCode"),
    path("updateCode/<uuid:id>", UpdateCode, name="updatecode"),
    path("mycode/", MyCodesView, name="mycode"),
    path("opencode/<uuid:id>", OpenCodeView, name="opencode"),
    path("profile/", ProfileView, name="profile"),
    path("new/", newprofileView.as_view(), name="np"),
    # path("profile/", UpdateProfileView, name="updateprofilr"),
    
    
]

