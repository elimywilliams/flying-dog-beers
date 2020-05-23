#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:48:24 2020

@author: emilywilliams
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 11:29:59 2020

@author: emilywilliams
"""
import pandas as pd

#file_name = '/Users/emilywilliams/Documents/GitHub/SC_covid/countryLags.csv'
file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/countryLags.csv'
countryLags = pd.read_csv(file_name)
countryLags['Date'] = countryLags['Date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/allStateLags.csv'
#file_name = '/Users/emilywilliams/Documents/GitHub/SC_covid/allStateLags.csv'
stateLags = pd.read_csv(file_name)
stateLags['Date'] = stateLags['datetest'].astype('datetime64[ns]')



import dash
import dash_html_components as html
import dash_core_components as dcc

import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
from plotly.subplots import make_subplots


from dash.dependencies import Input, Output


import plotly.express as px
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

myList = ['A', 'B']
myDict = {'A': [1,2,3],'B': [4,5,6] }
default_category = 'A'
default_index = 0
countryOPTS = [{'label': 'Spain', 'value': 'Spain'},
            {'label': 'Italy', 'value': 'Italy'},
            {'label': 'Sweden', 'value': 'Sweden'},
            {'label': 'Switzerland', 'value': 'Switzerland'},
            {'label': 'Australia', 'value': 'Australia'},
            {'label': 'Austria', 'value': 'Austria'},
            {'label': 'France', 'value': 'France'},
            {'label': 'Germany', 'value': 'Germany'},
            {'label': 'Turkey', 'value': 'Turkey'},
            {'label': 'United States of America', 'value': 'US'},
            {'label': 'New Zealand', 'value': 'New Zealand'},
            {'label': 'United Kingdom', 'value': 'UK'},
            {'label': 'Mexico', 'value': 'Mexico'}]


stateOPTS = [
    {'label':'Arkansas','value':"AR"},
    {'label':'Alabama','value':"AL"},
    {'label':'Alaska','value':"AK"},

    {'label':'Arizona','value':"AZ"},
    {'label':'Connecticut','value':'CT'},
    {'label':'California','value':'CA'},
    {'label':'Colorado','value':"CO"},
    {'label':'Delaware','value':"DE"},

    {'label':'Florida','value':"FL"},
    {'label':'Georgia','value':"GA"},
    {'label':'Hawaii','value':'HI'},
    {'label':'Idaho','value':"ID"},

    {'label':'Illinois','value':"IL"},
    {'label':'Indiana','value':'IN'},
    {'label':'Iowa','value':"IA"},
    {'label':'Kansas','value':"KS"},

    {'label':"Kentucky",'value':"KY"},
    {'label':'Louisianna','value':"LA"},
    {'label':"Massachusetts",'value':"MA"},
    {'label':'Maine','value':"ME"},
    {'label':'Maryland','value':"MD"},

    {'label':'Michigan','value':"MI"},

    {'label':'Minnesota','value':"MN"},
    {'label':'Mississippi','value':'MS'},
    {'label':'Missouri','value':'MO'},
    {'label':'Montana','value':"MT"},
    {'label':'North Dakota','value':"ND"},
    {'label':'Nebraska','value':"NE"},

    {'label':'Nevada','value':"NV"},
    {'label':'New Hampshire','value':"NH"},
    

    {'label':'New Jersey','value':'NJ'},
    {'label':'New Mexico','value':"NM"},

    {'label':'New York','value':"NY"},
    {'label':'North Carolina','value':'NC'},
    {'label':'Ohio','value':"OH"},
    {'label':'Oklahoma','value':"OK"},
    {'label':'Oregon','value':'OR'},
    {'label':'Pennsylvania','value':'PA'},
    {'label':'Rhode Island','value':"RI"},
    {'label':'South Carolina','value':'SC'},
    {'label':'South Dakota','value':"SD"},
    {'label':'Tennessee','value':"TN"},
    {'label':'Texas','value':'TX'},
    {'label':'Vermont','value':"VT"},

    {'label':'Virginia','value':"VA"},
    {'label':'Washington','value':'WA'},
    {'label':'West Virginia','value':"WV"},

    {'label':'Wisconsin','value':'WI'},
    {'label':'Wyoming','value':'WY'}  
    ]




projOPTS = [
            {'label': 'Con Edison', 'value': 'ConEd'},
            {'label': 'Duke Ohio', 'value': 'DukeOH'},
            {'label': 'Dom Questar (UT)', 'value': 'DomQuest'},
            {'label': 'WEC Energy (WI)', 'value': 'WEC_WI'},
            {'label': 'WPS MMD (WI)', 'value': 'WPS_WI'},
            {'label': 'Peoples (IL)', 'value': 'PeoplesIL'},
            {'label': 'ACLARA (NY)))', 'value': 'Aclara'},
            {'label': 'Duke IPI', 'value': 'DukeIPI'},
            {'label': 'Norwhich Public Utilities', 'value': 'norwhich'},
            {'label': 'Trussville (AL)', 'value': 'Trussville'},
            {'label': 'CPS (TX)))', 'value': 'CPS_TX'},
            {'label': 'Dominion (SC)', 'value': 'DominionSC'},
            {'label': 'Dominion (NC)', 'value': 'DominionNC'}
        ]




whichAvgOPTS = [
        {'label': '7 Day ', 'value': 'sevenday'},
        {'label': '3 Day', 'value': 'threeday'},
        {'label': 'Daily', 'value': 'daily'},
        {'label': 'Cumulative','value':'total'}
    ]

popOPTS = [
    {'label':'Relative to Population','value':'relpop'},
    {'label':'Raw Cases', 'value':'nonrelpop'}
    
    
    ]

tab1 = html.Div([
    html.H3('Country by Country Information'),
    dcc.Dropdown(id='countryChoice',
                 options= countryOPTS,
                 value = 'US'
    ),
     dcc.RadioItems(
        id = 'whichAvg2',
    options= whichAvgOPTS,
    value='sevenday',  labelStyle={'display': 'inline-block'}

    ),
     dcc.RadioItems(
         id = 'popratio2',
         options = popOPTS,
         value='relpop',
         labelStyle = {'display':'inline-block'}
         ),
    dcc.Graph(id='graph_close')
    
])




tab2 = html.Div([
    html.H3('State by State Information'),
     dcc.Dropdown(id='stateChoice',
                 options= stateOPTS,
                 value = 'CO'
    ),
    dcc.RadioItems(
        id = 'whichAvg',
    options= whichAvgOPTS,
    value='threeday',  labelStyle={'display': 'inline-block'}

    ) , 
    dcc.RadioItems(
        id = 'popratio',
        options = popOPTS,
        value = 'relpop',
        labelStyle = {'display':'inline-block'}
        ),
    dcc.Graph(id='state_graph')
])    


tab3 = html.Div([
    html.H3('SC Project Information'),
    dcc.Dropdown(
        id = 'whichProj',
        options = projOPTS,
        value = 'ConEd'
        )


    
    
    
    ])

app.layout = html.Div([
    html.H1('Southern Cross Covid Information'),
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(id="tab-1", label='Country', value='tab-1-example'),
        dcc.Tab(id="tab-2", label='State', value='tab-2-example'),
        dcc.Tab(id='tab-3',label='Project',value = 'tab-3-example')
    ]),
    html.Div(id='tabs-content-example',
             children = tab1)
])

@app.callback(dash.dependencies.Output('tabs-content-example', 'children'),
             [dash.dependencies.Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1
    elif tab == 'tab-2-example':
        return tab2
    elif tab == 'tab-3-example':
        return tab3

# =============================================================================
# @app.callback(
#     [dash.dependencies.Output('second-dropdown', 'options'),
#      dash.dependencies.Output('second-dropdown', 'value')],
#     [dash.dependencies.Input('countryChoice', 'value')])
# def update_dropdown(value):
#     return [[ {'label': i, 'value': i} for i in myDict[value] ], myDict[value][default_index]]
# 
# =============================================================================

@app.callback(dash.dependencies.Output('graph_close', 'figure'),
              [dash.dependencies.Input('countryChoice', 'value'),
               dash.dependencies.Input('whichAvg2','value'),
               dash.dependencies.Input('popratio2','value')
               ])


def update_country_fig(input_value,which_avg,pop_rat):
    df = countryLags[countryLags.Country_Region == input_value]
    if which_avg == 'sevenday':
        xvals = df.Date
        yvalDeaths = df.death_7
        yvalCases = df.mean_7
        title = 'Weekly Cases and Deaths, ' + input_value
        yCaseTitle = "Weekly Cases"
        yDeathTitle = "Weekly Deaths"
    elif which_avg == 'threeday':
        xvals = df.Date
        yvalDeaths = df.death_3
        yvalCases = df.mean_3
        title = 'Three-Day Cases and Deaths, ' + input_value
        yCaseTitle = "Three-Day Cases"
        yDeathTitle = "Three-Day Deaths"
    elif which_avg == 'daily':
        xvals = df.Date
        yvalDeaths = df.newDeath
        yvalCases = df.newConfirmed
        title = 'Daily Cases and Deaths, ' + input_value
        yCaseTitle = "Daily Cases"
        yDeathTitle = "Daily Deaths"   
    elif which_avg == 'total':
        xvals = df.Date
        yvalDeaths = df.DeathCountry
        yvalCases = df.ConfirmedCountry
        title = 'Total Cases and Deaths, ' + input_value
        yCaseTitle = "Total Cases"
        yDeathTitle = "Total Deaths"
    if pop_rat == 'relpop':
        yvalDeaths = (yvalDeaths/df.Population)*1e5
        yvalCases = (yvalCases/df.Population)*1e5
        #title = title + 'per 100k people'
        yCaseTitle = yCaseTitle + ' per 100k'
        yDeathTitle = yDeathTitle + ' per 100k'
    
    
        
    # Create traces
    death_data = go.Scatter(
         x= xvals,
         y= yvalDeaths,
         name='Deaths',
         yaxis = 'y2'
     )
    mean_data = go.Scatter(
         x=xvals,
         y=yvalCases,
         name='Cases'
         # yaxis='y2'
     )
     # How do I integrate the layout?
    layout = go.Layout(
         title=title,
         yaxis=dict(
             title=yCaseTitle
         ),
         yaxis2=dict(
             title=yDeathTitle,
             overlaying='y',
             side='right'
         )
     )
       
    #data = []
# =============================================================================
#     trace_close = go.Scatter(
#         x = list(df.Date),
#         y = list(df.mean_7),
#         name = 'graph_close',
#         line = dict(color = '#f44242')
#         
#         )
# =============================================================================
    

# =============================================================================
#     # Create traces
#     death_data = go.Scatter(
#         x=df.Date,
#         y=df.death_7,
#         name='Deaths',
#         yaxis = 'y2'
#     )
#     mean_data = go.Scatter(
#         x=df.Date,
#         y=df.mean_7,
#         name='Cases'
#         # yaxis='y2'
#     )
#     # How do I integrate the layout?
#     layout = go.Layout(
#         title='Weekly Cases and Deaths, ' + input_value,
#         yaxis=dict(
#             title='Weekly Cases'
#         ),
#         yaxis2=dict(
#             title='Weekly Deaths',
#             overlaying='y',
#             side='right'
#         )
#     )
# =============================================================================
    data = [mean_data,death_data]
    
    #title = "Weekly New Cases, "+ input_value
    #data.append(trace_close)
   # layout= {'title':title,
    #         }
    return{
        'data':data,
        'layout': layout
        }

@app.callback(dash.dependencies.Output('state_graph', 'figure'),
              [dash.dependencies.Input('stateChoice', 'value')     ,
               dash.dependencies.Input('whichAvg','value'),
               dash.dependencies.Input('popratio','value')
               ])

def update_state_fig(input_value,which_avg,pop_rat):
    df = stateLags[stateLags.State == input_value]
    
    if which_avg == 'sevenday':
        xvals = df.Date
        yvalDeaths = df.death_7
        yvalCases = df.mean_7
        title = 'Weekly Cases and Deaths, ' + input_value
        yCaseTitle = "Weekly Cases"
        yDeathTitle = "Weekly Deaths"
    elif which_avg == 'threeday':
        xvals = df.Date
        yvalDeaths = df.death_3
        yvalCases = df.mean_3
        title = 'Three-Day Cases and Deaths, ' + input_value
        yCaseTitle = "Three-Day Cases"
        yDeathTitle = "Three-Day Deaths"
    elif which_avg == 'daily':
        xvals = df.Date
        yvalDeaths = df.newDeath
        yvalCases = df.newConfirmed
        title = 'Daily Cases and Deaths, ' + input_value
        yCaseTitle = "Daily Cases"
        yDeathTitle = "Daily Deaths"   
    elif which_avg == 'total':
        xvals = df.Date
        yvalDeaths = df.DeathState
        yvalCases = df.ConfirmedState
        title = 'Total Cases and Deaths, ' + input_value
        yCaseTitle = "Total Cases"
        yDeathTitle = "Total Deaths"
    if pop_rat == 'relpop':
        yvalDeaths = (yvalDeaths/df.Population)*1e5
        yvalCases = (yvalCases/df.Population)*1e5
        #title = title + 'per 100k people'
        yCaseTitle = yCaseTitle + ' per 100k'
        yDeathTitle = yDeathTitle + ' per 100k'

        
    # Create traces
    death_data = go.Scatter(
         x= xvals,
         y= yvalDeaths,
         name='Deaths',
         yaxis = 'y2'
     )
    mean_data = go.Scatter(
         x=xvals,
         y=yvalCases,
         name='Cases'
         # yaxis='y2'
     )
     # How do I integrate the layout?
    layout = go.Layout(
         title=title,
         yaxis=dict(
             title=yCaseTitle
         ),
         yaxis2=dict(
             title=yDeathTitle,
             overlaying='y',
             side='right'
         )
         #,
         #legend_orientation="h"

     )
        
        
# =============================================================================
#     
#     if which_avg == 'sevenday':
#          # Create traces
#         death_data = go.Scatter(
#             x=df.Date,
#             y=df.death_7,
#             name='Deaths',
#             yaxis = 'y2'
#         )
#         mean_data = go.Scatter(
#             x=df.Date,
#             y=df.mean_7,
#             name='Cases'
#             # yaxis='y2'
#         )
#         # How do I integrate the layout?
#         layout = go.Layout(
#             title='Weekly Cases and Deaths, ' + input_value,
#             yaxis=dict(
#                 title='Weekly Cases'
#             ),
#             yaxis2=dict(
#                 title='Weekly Deaths',
#                 overlaying='y',
#                 side='right'
#             )
#         )
#     elif which_avg == 'threeday':
#          # Create traces
#         death_data = go.Scatter(
#             x=df.Date,
#             y=df.death_3,
#             name='Deaths',
#             yaxis = 'y2'
#         )
#         mean_data = go.Scatter(
#             x=df.Date,
#             y=df.mean_3,
#             name='Cases'
#             # yaxis='y2'
#         )
#         # How do I integrate the layout?
#         layout = go.Layout(
#             title='Three-Day Cases and Deaths, ' + input_value,
#             yaxis=dict(
#                 title='3 Day Cases'
#             ),
#             yaxis2=dict(
#                 title='3 Day Deaths',
#                 overlaying='y',
#                 side='right'
#             )
#         )
#     elif which_avg == 'daily':
#          # Create traces
#         death_data = go.Scatter(
#             x=df.Date,
#             y=df.newDeath,
#             name='Deaths',
#             yaxis = 'y2'
#         )
#         mean_data = go.Scatter(
#             x=df.Date,
#             y=df.newConfirmed,
#             name='Cases'
#             # yaxis='y2'
#         )
#         # How do I integrate the layout?
#         layout = go.Layout(
#             title='Daily New Cases and Deaths, ' + input_value,
#             yaxis=dict(
#                 title='Daily Cases'
#             ),
#             yaxis2=dict(
#                 title='Daily Deaths',
#                 overlaying='y',
#                 side='right'
#             )
#         )
#     elif which_avg == 'total':
#          # Create traces
#         death_data = go.Scatter(
#             x=df.Date,
#             y=df.DeathState,
#             name='Deaths',
#             yaxis = 'y2'
#         )
#         mean_data = go.Scatter(
#             x=df.Date,
#             y=df.ConfirmedState,
#             name='Cases'
#             # yaxis='y2'
#         )
#         # How do I integrate the layout?
#         layout = go.Layout(
#             title='Cases and Deaths, ' + input_value,
#             yaxis=dict(
#                 title='Total Cases'
#             ),
#             yaxis2=dict(
#                 title='Deaths',
#                 overlaying='y',
#                 side='right'
#             )
#         )
# =============================================================================
    #data = []inpu
# =============================================================================
#     trace_close = go.Scatter(
#         x = list(df.Date),
#         y = list(df.mean_7),
#         name = 'graph_close',
#         line = dict(color = '#f44242')
#         
#         )
# =============================================================================
    

# =============================================================================
#     # Create traces
#     death_data = go.Scatter(
#         x=df.Date,
#         y=df.death_7,
#         name='Deaths',
#         yaxis = 'y2'
#     )
#     mean_data = go.Scatter(
#         x=df.Date,
#         y=df.mean_7,
#         name='Cases'
#         # yaxis='y2'
#     )
#     # How do I integrate the layout?
#     layout = go.Layout(
#         title='Weekly Cases and Deaths, ' + input_value,
#         yaxis=dict(
#             title='Weekly Cases'
#         ),
#         yaxis2=dict(
#             title='Weekly Deaths',
#             overlaying='y',
#             side='right'
#         )
#     )
# =============================================================================
    data = [mean_data,death_data]
    
    #title = "Weekly New Cases, "+ input_value
    #data.append(trace_close)
   # layout= {'title':title,
    #         }
    return{
        'data':data,
        'layout': layout
        }


if __name__ == '__main__':
    app.run_server(debug=False)
