from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import  logout
from django.shortcuts import render , redirect
from django.http import JsonResponse
from django.contrib.auth import views as auth_view 
from django.core.paginator import Paginator
from.forms import *
from .models import *
import json 

def AvatarImageForBaseHTMLView(request):
    user = request.user
    consumer = Consumer.objects.get(user = user)
    return  render(request, 'base.html', {'consumer': consumer})
    
def LogoutView(request):
    logout(request)
    messages.success(request , " Sucessfully Loged-Out ! ")
    return redirect('login')

class MyPasswordChangeView(auth_view.PasswordChangeView):
    template_name = "PasswordChangeForm.html"
    form_class = MyPasswordChangeForm
    success_url = '/pwdchangedone/'

    def form_valid(self, form):
        user = form.save()
        # update_session_auth_hash(self.request, user)
        logout(self.request)  # Call your specific function here
        messages.success(self.request, 'Your password was successfully updated!')
        return super().form_valid(form)

class ConsumerRegistrationFormView(TemplateView):
    def get(self , request):
        form = ConsumerRegistrationForm()
        return render(request , "ConsumerRegistrationForm.html", {"form" : form} )
    
    def post(self , request):
        form = ConsumerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Consumer.objects.create(user=user)
            
            messages.success(request , " Congratulations :) Registered SucessFully ! Please Login ")
            form.save()
            return redirect('login')
        
        return render(request , "ConsumerRegistrationForm.html", {"form" : form} )
    
@csrf_exempt

def SaveCode(request):
    user  =  request.user
    data = json.loads(request.body)
    code = data.get('code')
    title  = data.get('title')
    language = data.get('language')
    if code and  title :

        MyCodes.objects.create(title = title , code = code , language = language ,user= user ) 
    
        return JsonResponse({'message': 'Code saved successfully :) ' , 'color' :'alert-success'}, status=201)
    else :
        return JsonResponse({'message' : ' Please enter some Code and Title :(' , 'color' :'alert-danger'}, status=400)
@csrf_exempt
def UpdateCode(request ,id ):
    user  =  request.user
    data = json.loads(request.body)
    
    code = data.get('code')
    title  = data.get('title')
    language = data.get('language')
    
    if code and  title :
        qset=  MyCodes.objects.get(id = id , user = user )
        qset.title = title
        qset.language = language
        qset.code = code
        qset.save()
        
    
        return JsonResponse({'message': 'Code saved successfully :) ' , 'color' :'alert-success'}, status=201)
    else :
        return JsonResponse({'message' : ' Please enter some Code and Title :(' , 'color' :'alert-danger'}, status=400)



class  MyCodesView(TemplateView):  
    def get(self, request) :
        user = request.user
        
       
        codes = MyCodes.objects.filter(user = user).order_by("-updated_at")
        if codes  :
            pages = Paginator(codes , 4)
            page_number =request.GET.get('page') 
            display_page  = pages.get_page(page_number)
            return render(request , "MyCodes.html" , {"mycodes" : display_page} )

        return render(request , "NoSavedCode.html" )
    def post(self, request) :
        user = request.user
        searchTitle = request.POST.get('searchTitle')
        if searchTitle :
            mycodes = MyCodes.objects.filter(user = user , title__icontains = searchTitle)
            if mycodes :
                return  render(request , "MyCodes.html" , {"mycodes" : mycodes} )
            return render(request , 'NoSavedCode.html')
        return redirect('mycode')


def OpenCodeView(request ,id):
    user  = request.user
    code = MyCodes.objects.get(user = user ,id = id)
    return render(request , "OpenCode.html" , {"code" : code} )

class ProfileView(TemplateView ) :
    def get(self , request) :
        user = request.user

        consumer, created = Consumer.objects.get_or_create(user = user) 

        if consumer:
            return render(request , "Profile.html" ,context= {'consumer' :consumer})
    
    def post(self , request) :
        user = request.user
        consumer, created = Consumer.objects.get_or_create(user = user) 
        if 'removeAvatar' in request.POST:
            consumer.avatar.delete()
            consumer.avatar = None  
            consumer.save()
            return redirect('profile') 



        name  =  request.POST.get('name')
        avatar = request.FILES.get('avatar')
        if name:
            consumer.name = name
        
        if avatar:
            consumer.avatar = avatar
        print("\n\n\n\n\n Saved And name is :" , name)
        consumer.save()
        return redirect('profile')
    


