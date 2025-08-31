from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny


from django.shortcuts import render
from .serializers import BookSerializer
from .models import Book

# Create your views here.
