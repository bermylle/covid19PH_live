from datasets.world_data import data_world

# DATA SETS FOR PH
ph_data = data_world["Philippines"] # SAMPLE DATA : {'date': '2020-5-15', 'confirmed': 12091, 'deaths': 806, 'recovered': 2460}

ph_dates = []
ph_dates_daily = []
ph_confirmed = []
ph_recoveries = []
ph_deaths = []

ph_confirmed_total = ph_data[-1]["confirmed"]
ph_recoveries_total = ph_data[-1]["recovered"]
ph_deaths_total = ph_data[-1]["deaths"]

for values in ph_data:
	if values["confirmed"] >= 100:
		ph_dates.append(values["date"])

for values in ph_data:
	if values["confirmed"] >= 100:
		ph_confirmed.append(values["confirmed"])

for values in ph_data:
	if values["confirmed"] >= 100:
		ph_recoveries.append(values["recovered"])

for values in ph_data:
	if values["confirmed"] >= 100:
		ph_deaths.append(values["deaths"])

for value in range(len(ph_data) - 19,len(ph_data)):
	if (value != len(ph_confirmed)):
		ph_dates_daily.append(ph_data[value]["date"])