from django import forms

class UserSearchForm(forms.Form):
    search = forms.CharField(max_length=100 , label="search" )