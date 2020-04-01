from app import app
from flask import Flask, render_template, request
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
import quandl
import requests
#quandl.ApiConfig.api_key = "visprKjKxPE5TXHoFLw5"

def getData(ticker):
    # api_url = 'https://www.quandl.com/api/v1/datasets/WIKI/%s.json' % ticker
    # session = requests.Session()
    # session.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
    # raw_data = session.get(api_url)
    dataSource = 'WIKI/' + ticker
    data = quandl.get(dataSource, rows=30)
    return data

def createFig(data,ticker):
    p = figure(title=ticker+' close', x_axis_type='datetime')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Close Price'
    p.line(data.index[-30:], data['Close'][-30:], line_width=2)
    return p

# @app.route('/')
# @app.route('/index')
# def index():
#     #ticker = 'GOOG'
#     ticker = request.args.get("ticker")
#     if ticker == None:
#         ticker = 'AAPL'
#     data = getData(ticker)
#     p = createFig(data,ticker)
    
#     # Embed plot into HTML via Flask Render
#     [script, div] = components(p)
    
#     return render_template("stock.html", script=script, div=div)

@app.route('/')
@app.route('/index')
def index():
    #ticker = 'GOOG'
    ticker = request.args.get("ticker")
    if ticker == None:
        ticker = 'AAPL'
    data = getData(ticker)
    p = createFig(data,ticker)
    
    # Embed plot into HTML via Flask Render
    [script, div] = components(p)
    
    return str(data['Close'][-1:])
