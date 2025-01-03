from django.urls import path
from .views import *

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('admin-pannel/', AdminPannel.as_view(), name='admin_pannel'),
    
    path('appointment/add', AddAppoint.as_view(), name='appoint_add'),
    path('appointment/<int:pk>', ViewAppoint.as_view(), name='appoint_view'),
    path('appointment/<int:pk>/update', UpdateAppoint.as_view(), name='appoint_update'),
    path('appointment/<int:pk>/delete', DeleteAppoint.as_view(), name='appoint_delete'),
]