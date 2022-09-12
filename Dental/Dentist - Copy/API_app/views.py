from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from Dentist_app.models import Patient
from Dentist_app.serializer import PatientSerializer
import pdb


@api_view(['GET', 'POST', 'DELETE'])
def patient_list(request):
    """
    Fetching Patient_app details form database and display output.
    And allow province to post new patient data and province ofr delete patient data.
    """
    pdb.set_trace()
    if request.method == 'GET':
        patients = Patient.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            patients = patients.filter(title__icontains=name)
        
        patients_serializer = PatientSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data)
        return JsonResponse(patient_serializer.errors)
    
    elif request.method == 'DELETE':
        count = Patient.objects.all().delete()
        return JsonResponse({'message': '{} Patient_app deleted successfully!'.format(count[0])})
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def patient_detail(request, pk):
    """
    For updating Patient_app data.
    """
    try: 
        patient = Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return JsonResponse({'message': 'The patient does not exist'})
 
    if request.method == 'GET': 
        patient_serializer = PatientSerializer(patient)
        return JsonResponse(patient_serializer.data)
 
    elif request.method == 'PUT': 
        patient_data = JSONParser().parse(request)
        patient_serializer = PatientSerializer(patient, data=patient_data)
        if patient_serializer.is_valid():
            patient_serializer.save()
            return JsonResponse(patient_serializer.data)
        return JsonResponse(patient_serializer.errors)
 
    elif request.method == 'DELETE': 
        patient.delete()
        return JsonResponse({'message': 'Patient_app was deleted successfully!'})
