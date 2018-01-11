from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Search
import requests
import urllib


def search_page(request):

	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			location = form.instance.location
			food = form.instance.food
			search = form.save()
			search.save()
			previous_searches = Search.objects.order_by('id')[:5]
			parameters = {
				'near': location,
				'query': food,
				'limit': 10,
				'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
				'v': '20180111'
			}
			url_params = urllib.parse.urlencode(parameters)
			request_url = 'https://api.foursquare.com/v2/venues/search?' + url_params
			response = requests.get(request_url)
			response = response.json()
			venues = response["response"]["venues"]
			venues_list = []
			for venue in venues:
				venues_list.append(venue['name'])
	else:
		venues_list = []
		form = SearchForm()

	return render(request, 'search_page.html', context={'form': form,
														'venues_list': venues_list, })
