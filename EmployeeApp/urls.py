from django.conf.urls import url
from EmployeeApp import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

url(r'^position/$',views.positionApi),
url(r'^position/([0-9]+)$',views.positionApi),

url(r'^employee/$',views.employeeApi),
url(r'^employee/([0-9]+)$',views.employeeApi)
]