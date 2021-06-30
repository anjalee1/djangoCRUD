from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Position,Employees
from EmployeeApp.serializers import PositionSerializer,EmployeeSerializer

# Create your views here.
@csrf_exempt
def positionApi(request,id=0):

    if request.method=='GET':
        positions = Position.objects.all()
        position_serializer = PositionSerializer(positions, many=True)
        return JsonResponse(position_serializer.data, safe=False) #safe parameter is used to inform django that what we are trying to convert to json
                                                             #is valid format and if there is still issue then we are ok with that.

    elif request.method=='POST':
        position_data=JSONParser().parse(request)
        position_serializer = PositionSerializer(data=position_data)
        if position_serializer.is_valid():
            position_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        position_data = JSONParser().parse(request)
        positions=Position.objects.get(PositionId=position_data['PositionId'])
        positions_serializer=PositionSerializer(positions,data=position_data )
        if positions_serializer.is_valid():
            positions_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        positions=Position.objects.get(PositionId=id)
        positions.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def employeeApi(request,id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee=Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer=EmployeeSerializer(employee,data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        employee=Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

