from covid import Covid
import flask
from flask import render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# by default data source is "john_hopkins"
covid = Covid()

# get ph data
ph_cases = covid.get_status_by_country_name("philippines")
active = covid.get_total_active_cases()

print(ph_cases['confirmed'])
# MAIN
@app.route('/', methods = ['POST', 'GET'])
def index():
	return render_template('index.html', cases = ph_cases)

@app.route('/ph')
def ph():
	return ph_cases

app.run()
