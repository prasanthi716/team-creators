from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def drivers(request):
    return render(request, "drivers/drivers.html")