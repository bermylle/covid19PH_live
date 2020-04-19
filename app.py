from covid import Covid
import flask
from flask import render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# by default data source is "john_hopkins"
covid = Covid()

# get ph data
ph_cases = covid.get_status_by_country_name("philippines")

# filtered_cases = { 'confirmed' : ph_cases.get("confirmed"),
# 'active' : ph_cases.get("active"), 'recovered' : ph_cases.get("recovered"), 'deaths' :  ph_cases.get("deaths") }

confirmed_case = {'confirmed' : ph_cases.get("confirmed")}
active_case = {'active' : ph_cases.get("active")}
recovered_case = {'recovered' : ph_cases.get("recovered")}
death_case = {'deaths' :  ph_cases.get("deaths")}


# MAIN
@app.route('/', methods = ['POST', 'GET'])
def index():
	return render_template('index.html', confirmed = confirmed_case, active = active_case, recovered = recovered_case, death = death_case)

@app.route('/ph')
def ph():
	return ph_cases

app.run()
