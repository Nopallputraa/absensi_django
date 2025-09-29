from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "landing/index.html", {
        "year": datetime.now().year
    })