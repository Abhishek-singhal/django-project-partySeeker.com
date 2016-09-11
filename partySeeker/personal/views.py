from django.shortcuts import render
import requests
import json
from django.http import HttpResponse

def index(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about-us.html')

def party(request):
    place = request.POST.get('place',None)
    url = "https://developers.zomato.com/api/v2.1/locations?query="+ str(place)
    header = {'User-Agent': 'curl/7.30.0', 'Accept': 'application/json', 'user_key': 'your user key provided by zomato',}
    r = requests.get(url=url, headers=header)
    res = r.json()
    entity_id = res['location_suggestions'][0]['entity_id']
    entity_type = res['location_suggestions'][0]['entity_type']
    url2 = "https://developers.zomato.com/api/v2.1/search?entity_id="+ str(entity_id)+"&entity_type="+ entity_type 
    r2 = requests.get( url=url2, headers=header)
    res2 = r2.json()
    Name_of_restaurant = []
    link = []
    Address = []
    Cuisines = []
    Cost_per_two = []
    pic = []
    for i in range (0,5):
	    Name_of_restaurant.append(res2['restaurants'][i]['restaurant']['name'])
	    link.append(res2['restaurants'][i]['restaurant']['url'])    
	    Address.append(res2['restaurants'][i]['restaurant']['location']['address'])
	    Cuisines.append(res2['restaurants'][i]['restaurant']['cuisines'])
	    Cost_per_two.append(res2['restaurants'][i]['restaurant']['average_cost_for_two'])
	    pic.append(res2['restaurants'][i]['restaurant']['thumb'])
    dic = {}
    dic['Name_of_restaurant'] = Name_of_restaurant
    dic['link'] = link
    dic['Address'] = Address
    dic['Cuisines'] = Cuisines
    dic['Cost_per_two']= Cost_per_two
    dic['pic'] = pic
    data = []
    data.append(dic)
    return render(request, 'personal/restaurants.html', {'data':data})