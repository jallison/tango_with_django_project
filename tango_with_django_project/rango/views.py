from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context_dict = {'boldmessage': "Cruncy, creamy, cookie, candy, cupcake!"}
    return render(request, 'index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage': "This is part of the tutorial!"}
    return render(request, 'about.html', context=context_dict)