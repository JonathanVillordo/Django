from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    name  = forms.CharField(max_length=128, help_text="Please enter Category.")
    view  = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug  = forms.CharField(widget=forms.HiddenInput(), required=False)

    #An inline class to provide addtional information on the form.
    class Meta:
        #Provide an association between the Modelform and a model.
        model  = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url   = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        #If url si not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://'+ url
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        #Provide an association between the Modelform and the models
        model = Page

        # what field do we want  to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hidding the foreign keyself.
        # we can either exlclude the category field from the form
        exclude = ('category',)
        # or specify the fields to include (i.e. not include the category field)
        # fields =('title', 'url', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('website','picture')
