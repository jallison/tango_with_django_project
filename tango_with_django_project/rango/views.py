from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Create your views here.
def index(request):
    
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "This is part of the tutorial!"}
    return render(request, 'about.html', context=context_dict)