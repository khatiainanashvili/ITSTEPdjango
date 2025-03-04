from django import forms
from .models import Books

class BookForm(forms.ModelForm):

    author_name = forms.CharField(max_length=100, required=True) 

    class Meta:
        model = Books
        fields = ['title', 'author_name', 'description', 'genre', 'cover'] 


class BookUpdateForm(forms.ModelForm):
    class Meta: 
        model = Books
        fields = '__all__'