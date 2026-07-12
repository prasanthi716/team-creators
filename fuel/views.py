from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def fuel(request):
    return render(request, "fuel/fuel.html")