from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Appointment
from django.urls import reverse_lazy

class home(TemplateView):
    template_name = 'app/home.html'

class AdminPannel(ListView):
    model = Appointment
    context_object_name = 'appoint'
    template_name = 'app/admin-pannel.html'

class AddAppoint(CreateView):
    model = Appointment
    fields = ['patient','doctor','appointment_time','status','reason']
    template_name = 'app/add-appoint.html'

class ViewAppoint(DetailView):
    model = Appointment
    context_object_name = 'appoint'
    template_name = 'app/view-appoint.html'

class UpdateAppoint(UpdateView):
    model = Appointment
    fields = ['patient','doctor','appointment_time','status','reason']
    template_name = 'app/update-appoint.html'

class DeleteAppoint(DeleteView):
    model = Appointment
    template_name = 'app/delete-appoint.html'
    success_url = reverse_lazy('admin_pannel')


