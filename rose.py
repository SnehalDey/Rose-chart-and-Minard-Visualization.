import numpy as np
import pandas as pd
import plotly
#plotly.offline.init_notebook_mode(connected=True)
import plotly.offline as py
import plotly.graph_objs as go
from plotly import tools

dataset = pd.read_csv('C:/Users/BadBoy/Desktop/nightingale.csv', header=1)

first = go.Barpolar(
   r = dataset['All other causes.1'][0:12],
   theta=dataset['Month'][0:12],
    marker = dict(
        color = '#cf3317', 
        opacity = 0.7),  
    name = 'All other causes', 
    showlegend = True,
    subplot = 'polar1',)

second = go.Barpolar(
    r = dataset['Zymotic diseases.1'][0:12],
    theta = dataset['Month'][0:12],
    marker = dict(
        color = '#17cccf', 
        opacity = 0.7), 
    name = 'Zymotic diseases', 
    showlegend = True,
    subplot = 'polar1',)


third = go.Barpolar(
    r = dataset['Wounds & injuries.1'][0:12],
    theta = dataset['Month'][0:12],
    marker = dict(
        color = '#a1cf17', 
        opacity = 0.7 ), 
    name = 'Wounds & injuries', 
    showlegend = True,
    subplot = 'polar1')



fourth = go.Barpolar(
    r = dataset['All other causes.1'][12:],
    theta = dataset['Month'][12:],
    marker = dict(
        color = '#cf3317', 
        opacity = 0.7 ), 
    name = 'All other causes', 
    showlegend = False,
    subplot = 'polar2')

fifth = go.Barpolar(
    r = dataset['Zymotic diseases.1'][12:],
    theta = dataset['Month'][12:],
    marker = dict(
        color = '#17cccf', 
        opacity = 0.7 ), 
    name = 'Zymotic diseases', 
    showlegend = False,
    subplot = 'polar2')

sixth = go.Barpolar(
    r = dataset['Wounds & injuries.1'][12:],
    theta = dataset['Month'][12:],
    marker = dict(
        color = '#a1cf17', 
        opacity = 0.7 ), 
    name = 'Wounds & injuries', 
    showlegend = False,
    subplot = 'polar2')



Plot_data = [first,second,third,fourth,fifth,sixth]

layout = dict (
    polar1 = dict(
      domain = dict(
        x = [0, 0.4],
        y = [0, 1] ),
      radialaxis = dict(
          visible = False ),
      angularaxis = dict(
          showgrid = True,
          ticks = "",
        thetaunit = "radians" ) ),
 polar2 = dict(
      domain = dict(
        x = [0.6, 1],
        y = [0, 1] ),
      radialaxis = dict( visible = False ),
      angularaxis = dict(
          showgrid = True,
          ticks = "",
          rotation = 180,
      thetaunit = "radians" )),
    width = 1000,
    height = 700,
    title = dict(
        text = 'DIAGRAM OF THE CAUSES OF MORTALITY IN THE ARMY IN THE EAST',
        font = dict(
            size = 20,
            family = "sans-serif",),
        xanchor='left' ))


fig = go.Figure(data=Plot_data, layout=layout)
plot_url = py.iplot(fig, validate=False)
