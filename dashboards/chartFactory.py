from bokeh.charts import Donut, Bar, show, output_file
from bokeh.embed import file_html, components
from bokeh.resources import CDN

import pandas as pd

import os
        
def bar_chart(dataset_path, var_name, threshold = 0.01):
    """
        dataset_path : The path to the dataset we're trying to build
        var_name : The name of the variable we are choosing to display a bar chart about
    """
    
    data = pd.read_csv(dataset_path, sep=';', encoding='latin-1')

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
    bar = Bar(data,title=" Chamadas por Bairro", legend=None)
    #html = file_html(bar, CDN)
    script, div = components(bar)

    return script, div


def donut_chart(dataset_path, var_name, threshold= 0.01):
    pass



    