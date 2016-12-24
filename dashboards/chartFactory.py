from bokeh.charts import Donut, Bar, show, output_file
from bokeh.embed import file_html, components
from bokeh.resources import CDN

import pandas as pd

import os
        
def make_chart(dataset_path, chart_type,  var_name = None, threshold = 0.01):
    if chart_type == 'bar':
        return bar_chart(dataset_path, var_name, threshold)
    elif chart_type == 'donut':
        return donut_chart(dataset_path, var_name, threshold)

def bar_chart(dataset_path, var_name = None, threshold = 0.01):
    """
        dataset_path : The path to the dataset we're trying to build
        var_name : The name of the variable we are choosing to display a bar chart about
    """
    
    data = pd.read_csv(dataset_path, sep=';', encoding='latin-1')
    if var_name is None:
        var_name = data.columns.tolist()[0]
        
    statistics = {}

    for item in data[var_name]:
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


def donut_chart(dataset_path, var_name, threshold= 0.01):
    
    statistics = {}
    data = pd.read_csv(dataset_path, sep=';', encoding='latin-1')

    if var_name is None:
        var_name = data.columns.tolist()[0]
        
    for item in data[var_name]:
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



    