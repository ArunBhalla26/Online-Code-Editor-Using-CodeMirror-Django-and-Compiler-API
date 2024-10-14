from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from django.shortcuts import render 
import json
import requests
from Codes.models import *
import os 

class IndexView(TemplateView):
    def get(self, request) :
        user = request.user
        if user.is_authenticated :
            consumer = Consumer.objects.get(user = user)
            return  render(request, 'index.html', {'consumer': consumer})
        else :
            return render(request, 'index.html')
        template_name = "index.html"
API_KEY = os.getenv('API_KEY')

   

def submit_code(code, language):
    if language == "python" :
       
        URL = API_HOST = "python-3-code-compiler.p.rapidapi.com/"
        payload = {
            "code": code ,
            "version": "latest",
            "input": None
        }


    elif language == "java" :

        URL = API_HOST = "java-code-compiler.p.rapidapi.com"
        payload = {
        "code": code,        
        "version": "latest"
        }
          
    elif language == "cpp" :
        URL = API_HOST = "cpp-17-code-compiler.p.rapidapi.com"
        payload = {"code": code,
                "version": "latest"
            }
        
    elif language == "c" :
        URL = API_HOST = "c-code-compiler.p.rapidapi.com"
        payload = {"code":code,
                "version": "latest"
            }
    else :
        URL = API_HOST = "c-sharp-code-compiler.p.rapidapi.com"
        payload = {"code": code,
                "version": "latest"
            }
        
    headers = {
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": API_HOST,
            "Content-Type":  "application/json"
        } 


        
    
    response = requests.post(f'https://{URL}', headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error submitting code: {response.text}")

@csrf_exempt
@require_POST
def compile_code(request):
    try:
       
        data = json.loads(request.body)
        code = data.get('code')
        language = data.get('language').lower()
        # stdin = data.get('stdin', '') 

        if not code or not language:
            return JsonResponse({'error': 'Code and language are required.'}, status=400)

       
        result = submit_code(code, language)
        
        if language == "python" :
            output = result.get('output') 

        elif language in  ["java", "cpp", "c","csharp"]:
            output = result.get('output')
        # print("output =" , output)

        return JsonResponse({'output': output})
    
    except Exception as e:
        
        return JsonResponse({'error': str(e)}, status=500)

