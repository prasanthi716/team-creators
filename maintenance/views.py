from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def maintenance(request):
    return render(request, "maintenance/maintenance.html")