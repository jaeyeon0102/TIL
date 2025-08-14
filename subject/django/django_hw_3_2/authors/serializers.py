from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    # book_count = serializers.IntegerField(source = 'book_set.count',read_only=True)
    book_count = serializers.SerializerMethodField()
    def get_book_count(self, obj):
        '''
            obj : 이 시리얼라이저를 호출한 객체 (아마 author)
        '''
        return obj.book_count
    class Meta:
        model = Author
        fields = '__all__'


# class SomeSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     content = serializers.CharField()
#     opening_time = serializers.TimeField()

#     class Meta:
#         # fields = '__all__'
#         read_only_fields = ('opening_time') 