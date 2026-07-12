from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Maintenance
from .forms import MaintenanceForm

class MaintenanceListView(ListView):
    model = Maintenance
    template_name = 'maintenance/list.html'
    context_object_name = 'maintenances'
    # Meta ordering on the model already sorts newest first, but explicitly set here for clarity
    ordering = ['-start_date', '-id']

class MaintenanceCreateView(CreateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'maintenance/form.html'
    success_url = reverse_lazy('maintenance_list')

class MaintenanceUpdateView(UpdateView):
    model = Maintenance
    form_class = MaintenanceForm
    template_name = 'maintenance/form.html'
    success_url = reverse_lazy('maintenance_list')

def close_maintenance(request, pk):
    if request.method != 'POST':
        return HttpResponseNotAllowed(['POST'])
    maintenance = get_object_or_404(Maintenance, pk=pk)
    if maintenance.status == 'Open':
        maintenance.status = 'Closed'
        maintenance.save()
    return redirect('maintenance_list')

class MaintenanceDeleteView(DeleteView):
    model = Maintenance
    template_name = 'maintenance/confirm_delete.html'
    success_url = reverse_lazy('maintenance_list')
