from app import app
from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
import quandl
quandl.ApiConfig.api_key = "visprKjKxPE5TXHoFLw5"


def getData(ticker):
    dataSource = 'WIKI/' + ticker
    data = quandl.get(dataSource)
    return data

def createFig(data):
    p = figure(title=ticker+' close', x_axis_type='datetime')
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = 'Close Price'
    p.line(data.index[-30:], data['Close'][-30:], line_width=2)
    return p
