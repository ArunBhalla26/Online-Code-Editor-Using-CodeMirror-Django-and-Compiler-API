from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
import requests
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

# Replace with your actual API key and host
API_KEY = 'Enter API Key'

API_HOST = 'onecompiler-apis.p.rapidapi.com'
API_URL = '/api/v1/run'

def submit_code(code, language, stdin=""):
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': API_HOST,
        'Content-Type': 'application/json'
    }
    
    payload = {
        'language': language.lower(),  # Convert language to lowercase as required by API
        'stdin': stdin,
        'files': [{
            'name': 'main',  # The file name used by the API
            'content': code
        }]
    }
    
    response = requests.post(f'https://{API_HOST}{API_URL}', headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error submitting code: {response.text}")

@csrf_exempt
@require_POST
def compile_code(request):
    try:
        # Load and parse request data
        data = json.loads(request.body)
        code = data.get('code')
        language = data.get('language')
        stdin = data.get('stdin', '')  # Default to empty string if not provided

        if not code or not language:
            return JsonResponse({'error': 'Code and language are required.'}, status=400)

        # Submit the code to the API
        result = submit_code(code, language, stdin)
        # print("result =" ,result )
        # Extract output from result
        output = result.get('stdout', '') or result.get('stderr', '') or result.get('error', '')
        # print("output =" , output)
        return JsonResponse({'output': output})
    
    except Exception as e:
        # Print error details for debugging
        # print(f"Error occurred: {e}")
        return JsonResponse({'error': str(e)}, status=500)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.decorators.http import require_POST
# import http.client
# import json , requests
# from django.views.generic import TemplateView


# class IndexView(TemplateView):
#     template_name = "index3.html"


# # Replace with your actual API key and host
# API_KEY = ''
# API_HOST = 'onecompiler-apis.p.rapidapi.com'
# API_URL = '/api/v1/run'

# def submit_code(code, language, stdin=""):
#     headers = {
#         'x-rapidapi-key': API_KEY,
#         'x-rapidapi-host': API_HOST,
#         'Content-Type': 'application/json'
#     }
#     print("lang:=",language.lower() )
#     print("code: = ", code , "\n code end")
#     payload = {
#         'language': language.lower(),  # Convert language to lowercase as required by API
#         'stdin': stdin,
#         'files': [{
#             'name': 'main',  # The file name used by the API
#             'content': code
#         }]
#     }
    
#     response = requests.post(f'https://{API_HOST}{API_URL}', headers=headers, json=payload)
    
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"Error submitting code: {response.text}")

# @csrf_exempt
# @require_POST
# def compile_code(request):
#     try:
#         # Load and parse request data
#         data = json.loads(request.body)
#         code = data.get('code')
#         language = data.get('language')
#         stdin = data.get('stdin', '')  # Default to empty string if not provided

#         if not code or not language:
#             return JsonResponse({'error': 'Code and language are required.'}, status=400)

#         # Submit the code to the API
#         result = submit_code(code, language, stdin)

#         # Extract output from result
#         output = result.get('stdout', '') or result.get('stderr', '')

#         return JsonResponse({'output': output})
    
#     except Exception as e:
#         # Print error details for debugging
#         print(f"Error occurred: {e}")
#         return JsonResponse({'error': str(e)}, status=500)

