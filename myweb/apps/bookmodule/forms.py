from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model= Book  
        fields='__all__'
        
    title= forms.CharField(max_length=100,required=True,label='Title',widget=forms.TextInput())
    author= forms.CharField(max_length=100,required=True,label='Author',widget=forms.TextInput())
    price = forms.DecimalField(required=True,label='Price',initial=0)
    edition = forms.IntegerField(required=True,label='Edition',initial=1,widget=forms.NumberInput())
    

