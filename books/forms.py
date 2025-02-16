from django import forms
from .models import Books

class BookForm(forms.ModelForm):

    author_name = forms.CharField(max_length=100, required=True) 
    country = forms.CharField(max_length=100, required=True) 

    class Meta:
        model = Books
        fields = ['title', 'author_name', 'country', 'description', 'genre'] 