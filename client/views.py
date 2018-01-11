from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import Search
import requests
import urllib


def search_page(request):
	form = SearchForm(request.GET)
	if form.is_valid():
		location = form.instance.location
		food = form.instance.food
		search = form.save()
		search.save()
		parameters = {
			'near': location,
			'query': food,
			'limit': 10,
			'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
			'v': '20180111'
		}
		url_params = urllib.parse.urlencode(parameters)
		request_url = 'https://api.foursquare.com/v2/venues/search?' + url_params
		venues_list = []
		response = requests.get(request_url)
		response = response.json()
		venues = response["response"]["venues"]

		for venue in venues:
			venue_info = {}
			venue_info['name'] = venue.get("name", "---")
			venue_info['phone'] = venue['contact'].get("formattedPone", "---")
			venue_info['checkin_count'] = venue['stats'].get('checkinsCount', "---")
			venues_list.append(venue_info)
	else:
		venues_list = []
		form = SearchForm()

	if Search.objects.count() > 5:
		previous_searches = Search.objects.order_by()[Search.objects.count() - 5:]
		previous_searches = previous_searches[::-1]  # reverses list
	else:
		previous_searches = Search.objects.order_by()[::-1]  # reverses list

	return render(request, 'search_page.html', context={'form': form,
														'venues_list': venues_list,
														'pre_searches': previous_searches})
