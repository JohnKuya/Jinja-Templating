from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def inner_page(request):
    return render(request, "inner-page.html")

def portfolio_details(request):
    return render(request, "portfolio-details.html")