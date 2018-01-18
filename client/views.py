from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .forms import SearchForm
from .models import Search
import requests
import urllib


def search_page(request):
	form = SearchForm(request.GET)
	if form.is_valid():
		location = form.instance.location
		food = form.instance.food
		last_search = Search.objects.order_by()[::-1][0]
		if last_search.location != location or last_search.food != food:
			search = form.save()
			search.save()
		parameters = {
			'near': location,
			'query': food,
			'limit': 100,
			'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
			'v': '20180111'
		}
		url_params = urllib.parse.urlencode(parameters)
		request_url = 'https://api.foursquare.com/v2/venues/search?' + url_params
		venues_list = []
		response = requests.get(request_url)
		response = response.json()
		venues = response.get("response").get("venues", [])

		if venues:
			for venue in venues:
				venue_info = {}
				venue_info['id'] = venue.get('id')
				venue_info['name'] = venue.get('name', "---")
				venue_info['phone'] = venue['contact'].get("formattedPone", "---")
				venue_info['checkin_count'] = venue['stats'].get('checkinsCount', "---")
				venues_list.append(venue_info)
	else:
		venues_list = []
		form = SearchForm()
		location = ""
		food = ""

	if venues_list:
		page = request.GET.get('page', 1)
		paginator = Paginator(venues_list, 10)  # pagination
		try:
			venues_list = paginator.page(page)
		except PageNotAnInteger:
			venues_list = paginator.page(1)
		except EmptyPage:
			venues_list = paginator.page(paginator.num_pages)

	if Search.objects.count() > 5:
		previous_searches = Search.objects.order_by()[Search.objects.count() - 5:]

	previous_searches = previous_searches[::-1]  # reverses list
	return render(request, 'search_page.html', context={'form': form,
														'venues_list': venues_list,
														'pre_searches': previous_searches,
														'searched_location': location,
														'searched_food': food})


def venue_detail(request, venue_id):
	parameters = {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'v': '20180111'
	}
	url_params = urllib.parse.urlencode(parameters)
	request_url = 'https://api.foursquare.com/v2/venues/' + venue_id + '?' + url_params
	response = requests.get(request_url)
	response = response.json()
	venue_detail = {}
	venue_detail['name'] = response['response']['venue']['name']
	venue_detail['phone'] = response['response']['venue']['contact'].get("phone", "-")
	venue_detail['twitter'] = response['response']['venue']['contact'].get("twitter", "-")
	venue_detail['facebook'] = response['response']['venue']['contact'].get("facebook", "-")
	venue_detail['icon'] = response['response']['venue']['categories'][0]['icon'].get('prefix', 'default') + "bg_32.png"
	page = request.GET.get('page', 1)  # pagination
	offset = 1 + 5 * (int(page)-1)
	parameters = {
		'oauth_token': 'BIH2RYEL3G20JYPXJX4LNZ01EL3VTMC0QXDNOTZKE5NZRAJL',
		'v': '20180111',
		'limit': '5',
		'offset': offset,
	}

	url_params = urllib.parse.urlencode(parameters)
	request_url = 'https://api.foursquare.com/v2/venues/' + venue_id + "/tips?" + url_params
	response = requests.get(request_url)
	response = response.json()
	venue_tips = response['response']['tips']["items"]

	return render(request, 'venue_detail.html', context={'venue_detail': venue_detail, 'venue_tips': venue_tips,
														 'page': page})
