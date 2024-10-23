from django import forms
from .models import books

class BookForm(forms.ModelForm):
    class Meta:
        model = books
        fields = ('bookid', 'name','author','image', 'description')