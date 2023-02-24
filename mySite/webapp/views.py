from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")
def ben_facts(request):
    return render(request, "ben_facts.html")
def cv_page(request):
    return render(request, "cv_page.html")
# Create your views here.
