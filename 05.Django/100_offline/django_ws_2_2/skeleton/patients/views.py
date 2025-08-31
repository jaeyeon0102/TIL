from .models import Patient
from .serializers import PatientSerializer, PatientListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET","POST"])
def patient_list_create(request):
    if request.method == 'GET':
        queryset = Patient.objects.all()
        data = PatientListSerializer(queryset,many=True).data
        return Response(data, status= 201)
    elif request.method == 'POST':

        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

