from django.shortcuts import render

def vehicles(request):
    return render(request, "vehicles/vehicles.html")