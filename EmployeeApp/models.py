from django.db import models

# Create your models here.

    
class Position(models.Model):
    PositionId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    # Position= models.ForeignKey(Position,on_delete=models.CASCADE)#ON DELETE CASCADE is used in to delete the
    #                                                               #rows from the child table automatically, when the rows 
    #  
    Position=models.CharField(max_length=100)                      # from the parent table are deleted
    DateOfJoining = models.DateField()
    Contact = models.CharField(max_length=15)
   
   