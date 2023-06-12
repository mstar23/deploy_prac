from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_page(request):
    return render(request, 'first_page.html')

def main_page(request):
    return render(request, 'main_page.html')