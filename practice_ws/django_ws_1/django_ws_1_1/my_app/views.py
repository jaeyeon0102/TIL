from rest_framework.decorators import api_view
from django.http import JsonResponse

# Create your views here.
@api_view(['GET'])
def hello(request):
    if request.method == "GET":
        return JsonResponse({'message': 'Welcome to your very first Django project'})