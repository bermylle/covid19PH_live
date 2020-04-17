from covid import Covid
import flask
from flask import render_template


app = flask.Flask(__name__)
app.config["DEBUG"] = True


# by default data source is "john_hopkins"
covid = Covid()

# get ph data
ph_cases = covid.get_status_by_country_name("philippines")

active_cases = ph_cases["active"]

@app.route('/')
def index():
	return ph_cases

app.run()
