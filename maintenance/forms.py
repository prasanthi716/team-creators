from django import forms
from django.db.models import Q
from vehicles.models import Vehicle
from .models import Maintenance

class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = [
            'vehicle',
            'maintenance_type',
            'description',
            'cost',
            'start_date',
            'end_date',
            'status'
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 1. Vehicle Selection Filtering
        if self.instance and self.instance.pk:
            # Edit mode: show Available vehicles OR the currently assigned vehicle
            self.fields['vehicle'].queryset = Vehicle.objects.filter(
                Q(status='Available') | Q(pk=self.instance.vehicle.pk)
            )
        else:
            # Create mode: only show Available vehicles
            self.fields['vehicle'].queryset = Vehicle.objects.filter(status='Available')

        # 2. Automated Bootstrap Styling
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.Select):
                css_class = 'form-select'
            else:
                css_class = 'form-control'

            existing_class = field.widget.attrs.get('class', '')
            if existing_class:
                field.widget.attrs['class'] = f"{existing_class} {css_class}"
            else:
                field.widget.attrs['class'] = css_class

    def clean_vehicle(self):
        vehicle = self.cleaned_data.get('vehicle')
        if not vehicle:
            return vehicle

        # Allow the currently assigned vehicle when editing
        if self.instance and self.instance.pk and self.instance.vehicle == vehicle:
            return vehicle

        # For new assignments, reject any vehicle that is not Available
        if vehicle.status != 'Available':
            raise forms.ValidationError(
                f"Vehicle {vehicle.registration_number} is currently '{vehicle.status}' and cannot be assigned to new maintenance."
            )

        return vehicle
