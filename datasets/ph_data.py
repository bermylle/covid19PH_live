from datasets.world_data import data_world
from covid import Covid

# by default data source is "john_hopkins"
covid = Covid()

# get ph data
ph_cases = covid.get_status_by_country_name("philippines")

# JHU API
confirmed_case = ph_cases.get("confirmed")
active_case = ph_cases.get("active")
recovered_case = ph_cases.get("recovered")
death_case = ph_cases.get("deaths")



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

for value in range(len(ph_data) - 29,len(ph_data)):
	if (value != len(ph_confirmed)):
		ph_dates_daily.append(ph_data[value]["date"])


daily_count = []

for value in range(len(ph_confirmed) - 30,len(ph_confirmed)):
	if (value != len(ph_confirmed) - 1):
		daily_count.append(ph_confirmed[value + 1] - ph_confirmed[value])