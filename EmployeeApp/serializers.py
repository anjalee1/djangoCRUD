from rest_framework import serializers
from EmployeeApp.models import Position,Employees

class PositionSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Position
        # fields='__all__'
        fields = ('PositionId','title')



class EmployeeSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Employees
        # fields='__all__'
        fields = ('EmployeeId',
                  'EmployeeName',
                  'Position',
                  'DateOfJoining',
                  'Contact')




