from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','genres','published_date','borrowed','isbn']

# class BookBorrowSerializer(serializers.Serializer):
#     isbn = serializers.CharField(max_length=13)