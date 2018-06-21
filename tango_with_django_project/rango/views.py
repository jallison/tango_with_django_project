from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm


# Create your views here.
def index(request):
    # Query the database for a list of ALL categoris currently stored.
    # Order the categories by no. likes in descening order
    # Retrieve the top 5 only - or all if less than 5
    # Place the list in our context_dict dictinary
    # that will be passed to the template engine.
    
    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages':pages_list}

    # Render the response and send it back!
    return render(request, 'index.html', context_dict)

def about(request):
    context_dict = {'boldmessage': "This is part of the tutorial!"}
    return render(request, 'about.html', context=context_dict)

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exceptiono.
        # So the .get() methond returns one model instance or raises and exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # Note that filter() will return a list of page objects or an empty list
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages

        # We allso add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Cateogry.DoesNotExist:
        # We get here if we didn't find the specified category
        # Don't do anything-
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'category.html', context_dict)

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            #Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We coudl give a confirmation message
            # But since the most recent category added is on the index page
            # Then we can direct the user back to the index page.
            return index(request)
        else:
            # The suppplied form contained errors - 
            # just print them to the terminal.
            print(form.errors)

    # Will handle the bad form, new form, or
    # no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(reqeust, category_name_slug)

        else:
            print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'add_page.html', context_dict)
