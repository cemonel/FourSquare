from django import forms


class SearchForm(forms.Form):
		venue = forms.CharField(max_length=100, error_messages={'required': 'Please choose a star rating'})
		location = forms.CharField(max_length=100, error_messages={'required': 'Please choose a star rating'})
