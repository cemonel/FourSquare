from django import forms


class SearchForm(forms.Form):
		venue = forms.CharField(max_length=100, required=False)
		location = forms.CharField(max_length=100, required=False)
