from django.shortcuts import render
from django.http import JsonResponse
# RESTful한 API를 만들도록 해주는 famework
from rest_framework.decorators import api_view
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import books
import random
# Create your views here.

@api_view(['GET','POST'])
def index(request):
    if request.method == 'GET':
        book = random.choice(books.books)
        return JsonResponse(book) 