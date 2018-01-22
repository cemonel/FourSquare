from django import forms


class SearchForm(forms.Form):
		venue = forms.CharField(max_length=100, required=True)
		location = forms.CharField(max_length=100, required=True)
