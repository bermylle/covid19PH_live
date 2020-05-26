
import flask
from flask import render_template
from flask_mysqldb import MySQL

from datasets.ph_data import *

app = flask.Flask(__name__)
app.config["DEBUG"] = True





# MAIN
@app.route('/')
@app.route('/home')
def daily():
	return render_template('daily-graph.html', ph_confirmed = ph_confirmed, 
		ph_recoveries = ph_recoveries, 
		ph_deaths = ph_deaths, ph_dates_daily = ph_dates_daily, ph_dates = ph_dates,
		daily_count = daily_count,  


		confirmed = confirmed_case, 
		active = active_case, recovered = recovered_case, deaths = death_case)



if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)