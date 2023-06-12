from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_page(request):
    # return render(request, 'first_page.html')
    return HttpResponse('안녕 테스트얌 ㅎㅎ')