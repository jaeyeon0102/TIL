from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields ='__all__'
        # 자동으로 생성되는 필드는 읽기 전용으로,,
        read_only_fields = ['id','created_at']