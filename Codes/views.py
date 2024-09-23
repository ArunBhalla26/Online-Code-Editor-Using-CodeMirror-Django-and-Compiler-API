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
            messages.success(request , " Congratulations :) Registered SucessFully ! Please Login ")
            form.save()
        
        return render(request , "ConsumerRegistrationForm.html", {"form" : form} )
    
@csrf_exempt
def SaveCode(request):

    data = json.loads(request.body)
    code = data.get('code')
    title  = data.get('title')
    language = data.get('language')
    if code and  title :

        MyCodes.objects.create(title = title , code = code , language = language ) 
    
        return JsonResponse({'message': 'Code saved successfully :) ' , 'color' :'alert-success'}, status=201)
    else :
        return JsonResponse({'message' : ' Please enter some Code and Title :(' , 'color' :'alert-danger'}, status=400)
