from flask import Flask
from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import quandl
quandl.ApiConfig.api_key = "visprKjKxPE5TXHoFLw5"

app = Flask(__name__)

from app import routes
