import urllib.request, json 

with urllib.request.urlopen("https://pomber.github.io/covid19/timeseries.json") as url:
	data_world = json.loads(url.read().decode()) # dict
