from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import  logout
from django.shortcuts import render , redirect
from django.http import JsonResponse
from.forms import *
from .models import *
import json 
def LogoutView(request):
    logout(request)
    messages.success(request , " Sucessfully Loged-Out ! ")
    return redirect('login')

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

def  MyCodesView(request):  
    user = request.user
    # if user :
    mycodes = MyCodes.objects.filter(user = user)
    codes = MyCodes.objects.filter(user = user)
    return render(request , "MyCodes.html" , {"mycodes" : mycodes} )
    return render(request , "NoSavedCode.html" )

def OpenCodeView(request ,id):
    user  = request.user
    code = MyCodes.objects.get(user = user ,id = id)
    return render(request , "OpenCode.html" , {"code" : code} )

def ProfileView(request ) :
    user = request.user

    consumer = Consumer.objects.get(user = user) 
    if consumer:
        return render(request , "Profile.html" ,context= {'consumer' :consumer})
    return render(request , "NoProfile.html")


class newprofileView(TemplateView):
    def get(self , request):
        form = ProfileForm()
        return render(request , "newprofile.html", {"form" : form} )
    
    def post(self , request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = form.save()
                     
            messages.success(request , " Congratulations :) Changes Saved SucessFully ! ")
            form.save()
            return redirect('login')
        
        return render(request , "newprofile.html", {"form" : form} )
    