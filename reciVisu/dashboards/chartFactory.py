from bokeh.charts import Donut, Bar, show, output_file
from bokeh.embed import file_html, components
from bokeh.resources import CDN
import numpy as np
import pandas as pd

import os


def return_variables_types(dataset_path, var_name):
    data = pd.read_csv(dataset_path, sep=';', encoding='latin-1')
    
    if var_name is None:
        var_name = data.columns.tolist()[0]
       
    var_type = data[var_name].dtype

    if var_type == np.int64: #which means there is no chart_type available
        chart_types = []
        chart_types.append("bar")
        chart_types.append('donut')
    return chart_types

        
def make_chart(dataset_path, chart_type = "",  var_name = None, threshold = 0.01):
    data = pd.read_csv(dataset_path, sep=';', encoding='latin-1')
    
    if var_name is None:
        var_name = data.columns.tolist()[0]
       
    var_type = data[var_name].dtype
    
    if var_type == np.int64 and chart_type == "": #which means there is no chart_type available
        chart_type = "bar"

    if chart_type == 'bar':
        return bar_chart(data[var_name], threshold, var_name)
    elif chart_type == 'donut':
        return donut_chart(data[var_name], var_name, threshold)

def bar_chart(data, threshold = 0.001, var_name = ""):
    """
        dataset_path : The path to the dataset we're trying to build
        var_name : The name of the variable we are choosing to display a bar chart about
    """
    
   
        
    statistics = {}

    for item in data:
        if item in statistics.keys():
            statistics[item] = statistics[item]+1
        else:
            statistics[item] = 1

    keys = []
    values = []

    sum_values = sum(statistics.values())
    for key, value in statistics.items():
        if value/sum_values > threshold: #this way only those who are above the 1% threshold
            keys.append(key)
            values.append(value)

    data = pd.Series(values, index = keys) 
    chart = Bar(data,title="Bar Chart about "+ str(var_name), legend=None)
    #html = file_html(bar, CDN)
    script, div = components(chart)

    return script, div


def donut_chart(data, var_name,  threshold= 0.01):
    
    statistics = {}


        
    for item in data:
        if item in statistics.keys():
            statistics[item] = statistics[item]+1
        else:
            statistics[item] = 1

    keys = []
    values = []

    sum_values = sum(statistics.values())
    for key, value in statistics.items():
        if value/sum_values > threshold: #this way only those who are above the 1% threshold
            keys.append(key)
            values.append(value)

    data = pd.Series(values, index = keys) 
    chart = Donut(data,title="Donut Chart about "+ str(var_name))
    #html = file_html(bar, CDN)
    script, div = components(chart)

    return script, div



    