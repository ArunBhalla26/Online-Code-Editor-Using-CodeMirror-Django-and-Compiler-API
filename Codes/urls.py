
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
    path("mycode/", MyCodesView.as_view(), name="mycode"),
    path("opencode/<uuid:id>", OpenCodeView, name="opencode"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("accounts/pwdchange/", MyPasswordChangeView.as_view(), name="pwdchange"),
    path("pwdchangedone/",auth_view.PasswordChangeDoneView.as_view(template_name  = "index.html" ),
                                                                    name="pwdchangedone"),
    
    

]

