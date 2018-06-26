from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on teh form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',) 

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)   

    class Meta:
        # Provide an association between the ModelForm and a model Forms
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # We can either exclude the category field from the form,
        exclude = ('category',)
        # or specify the fields to include (i.e. not include the category field)
        # fields= ('title', 'url', 'views')

    def clean(self):

        # Had to search to understand the code below - found this in github

        # * The Form subclass's "clean()" method. This method can perform
        # any validation that requires access to multiple fields from the form at
        # once. This is where you might put in things to check that if field "A"
        # is supplied, field "B" must contain a valid e-mail address and the
        # like. The data that this method returns is the final "cleaned_data"
        # attribute for the form, so don't forget to return the full list of
        # cleaned data if you override this method (by default, "Form.clean()"
        # just returns "self.cleaned_data").

        cleaned_data = self.cleaned_data

        # again found in github search

        # By the time the form's "clean()" method is called, all the individual field
        # clean methods will have been run (the previous two sections), so
        # "self.cleaned_data" will be populated with any data that has survived so
        # far. So you also need to remember to allow for the fact that the fields you
        # are wanting to validate might not have survived the initial individual field
        # checks.

        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            # Always return the full collection of cleaned data.
            return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

