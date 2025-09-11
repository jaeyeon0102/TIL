from django.contrib import admin
from .models import Book

# Register your models here.
# 아싸리 
# 관리자 사이트에 등록 (저자 정보)
admin.site.register(Book)