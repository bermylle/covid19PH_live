from covid import Covid
import flask
from flask import render_template
from flask_mysqldb import MySQL

from datasets.ph_data import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# by default data source is "john_hopkins"
covid = Covid()

# get ph data
ph_cases = covid.get_status_by_country_name("philippines")

# Database for graphs

confirmed_case = {'confirmed' : ph_cases.get("confirmed")}
active_case = {'active' : ph_cases.get("active")}
recovered_case = {'recovered' : ph_cases.get("recovered")}
death_case = {'deaths' :  ph_cases.get("deaths")}

daily_count = []

for value in range(len(ph_confirmed) - 20,len(ph_confirmed)):
	if (value != len(ph_confirmed) - 1):
		daily_count.append(ph_confirmed[value + 1] - ph_confirmed[value])
	


# MAIN
@app.route('/')
@app.route('/home')
def index():
	return render_template('home.html', confirmed = confirmed_case, active = active_case, recovered = recovered_case, death = death_case)


@app.route('/total-graph')
def graphs():
	
	return render_template('total-graph.html', ph_confirmed = ph_confirmed, 
		ph_recoveries = ph_recoveries, ph_deaths = ph_deaths, ph_dates = ph_dates, daily_count = daily_count)

@app.route('/daily-graph')
def daily():
	
	return render_template('daily-graph.html', ph_confirmed = ph_confirmed, 
		ph_recoveries = ph_recoveries, ph_deaths = ph_deaths, ph_dates = ph_dates_daily, daily_count = daily_count)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
