#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:30:21 2020

@author: emilywilliams
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
#from dash.dependencies import Input, Output
import plotly.express as px
#import base64
#import json
#import bs4 as bs
#import requests
#from textwrap import dedent as d

px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/header2.css'  ,
                        'https://github.com/plotly/dash-app-stylesheets/blob/master/dash-oil-and-gas.css'
                        ]


file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/usoverall.csv'
usLagOverall = pd.read_csv(file_name)
usLagOverall['Date'] = usLagOverall['datetest'].astype('datetime64[ns]')
usLagOverall['newConfirmed'] = usLagOverall['confirmed_infectionsnz']
usLagOverall['confirmedCountry'] = usLagOverall['totCases']



file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/countryLags.csv'
countryLags = pd.read_csv(file_name)
countryLags['Date'] = countryLags['Date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/allStateLags.csv'
stateLags = pd.read_csv(file_name)
stateLags['Date'] = stateLags['datetest'].astype('datetime64[ns]')


file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/citiInfo.csv'
citInfo = pd.read_csv(file_name)
citInfo['Date'] = citInfo['Date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/uspreddat.csv'
predInf = pd.read_csv(file_name)
predInf['Date'] = predInf['date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/Summary_stats_all_locs.csv'
status = pd.read_csv(file_name)

projOPTS = [
            {'label': 'ACLARA (NY)', 'value': 'Aclara'},
            {'label': 'Con Edison', 'value': 'ConEd'},
            {'label': 'CPS (TX)', 'value': 'CPS_TX'},

            {'label': 'Dom Questar (UT)', 'value': 'DomQuest'},
            
            {'label': 'Dominion (NC)', 'value': 'DominionNC'},
            {'label': 'Dominion (SC)', 'value': 'DominionSC'},
            
            {'label': 'Duke IPI', 'value': 'DukeIPI'},
            {'label': 'Duke Ohio', 'value': 'DukeOH'},
            {'label': 'Norwhich Public Utilities', 'value': 'norwhich'},

            {'label': 'Peoples (IL)', 'value': 'PeoplesIL'},
            {'label': 'Trussville (AL)', 'value': 'Trussville'},

            {'label': 'WEC Energy (WI)', 'value': 'WEC_WI'},
            {'label': 'WPS MMD (WI)', 'value': 'WPS_WI'}
        ]

whichAvgOPTS = [
        {'label': '7 Day Total ', 'value': 'sevenday'},
        {'label': '3 Day Total', 'value': 'threeday'},
        {'label': 'Daily Cases', 'value': 'daily'},
        {'label': 'Cumulative Cases','value':'total'}
    ]

popOPTS = [
    {'label':'Relative to Population','value':'relpop'},
    {'label':'Raw Cases', 'value':'nonrelpop'}
    
    
    ]

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
    {'label':'North Carolina','value':'NC'},

    {'label':'North Dakota','value':"ND"},
    {'label':'Nebraska','value':"NE"},

    {'label':'Nevada','value':"NV"},
    {'label':'New Hampshire','value':"NH"},
    

    {'label':'New Jersey','value':'NJ'},
    {'label':'New Mexico','value':"NM"},

    {'label':'New York','value':"NY"},
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


#### importing project - specific updates
file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/projectUpdateInfo.csv'
file = pd.read_csv(file_name)

px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')



file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/cityProjLags.csv'
citLags= pd.read_csv(file_name)
citLags['Date'] = citLags['date'].astype('datetime64[ns]')


trussProj = citLags[citLags.Province_State.isin(['Alabama'])].Combined_Key.unique()
trussOptions=[{'label': i, 'value': i} for i in trussProj]
        
conEDProj = citLags[citLags.Province_State.isin(['New York'])].Combined_Key.unique()
conEDProjOptions=[{'label': i, 'value': i} for i in conEDProj]


wisProj = citLags[citLags.Province_State.isin(['Wisconsin'])].Combined_Key.unique()
wisProjOptions=[{'label': i, 'value': i} for i in wisProj]


ohstates = ['Ohio','Kentucky','Indiana']
ohProj = citLags[citLags.Province_State.isin(ohstates)].Combined_Key.unique()
ohProjOptions=[{'label': i, 'value': i} for i in ohProj]


utProj = citLags[citLags.Province_State.isin(['Utah',"Idaho"])].Combined_Key.unique()
utProjOptions=[{'label': i, 'value': i} for i in utProj]


ilProj = citLags[citLags.Province_State.isin(['Illinois',"Wisconsin","Indiana"])].Combined_Key.unique()
ilProjOptions=[{'label': i, 'value': i} for i in ilProj]


aclaraProj = citLags[citLags.Province_State.isin(['New York'])].Combined_Key.unique()
aclaraProjOptions=[{'label': i, 'value': i} for i in aclaraProj]

norProj = citLags[citLags.Province_State.isin(['Rhode Island',"Connecticut"])].Combined_Key.unique()
norProjOptions=[{'label': i, 'value': i} for i in norProj]


texProj = citLags[citLags.Province_State.isin(['Texas'])].Combined_Key.unique()
texProjOptions=[{'label': i, 'value': i} for i in texProj]


norCarProj = citLags[citLags.Province_State.isin(['North Carolina'])].Combined_Key.unique()
norCarProjOptions=[{'label': i, 'value': i} for i in norCarProj]


southCarProj = citLags[citLags.Province_State.isin(['South Carolina'])].Combined_Key.unique()
southCarProjOptions=[{'label': i, 'value': i} for i in southCarProj]

fnameDict = {'ConEd': conEDProjOptions, 
             'DukeOH':ohProjOptions,
             'DomQuest':utProjOptions,
             'WEC_WI':wisProjOptions,
             'WPS_WI':wisProjOptions,
             'PeoplesIL':ilProjOptions,
             'Aclara':aclaraProjOptions,
             'DukeIPI':ohProjOptions,
             'norwhich':norProjOptions,
             'Trussville':trussOptions,
             'CPS_TX':texProjOptions,
             'DominionSC':southCarProjOptions,
             'DominionNC':norCarProjOptions
             }
names = list(fnameDict.keys())
nestedOptions = fnameDict[names[0]]


tab3=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Project Specific Information:", className="control_label"),
                       dcc.Dropdown(
                            id="whichProj",
                            #options=well_status_options,
                            options = projOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'DukeOH',
                            className="dcc_control",
                        ),
                        # html.P("Choose Related City:", className="control_label"),
                        # dcc.Dropdown(
                        #     id="whichCity",
                        #     #options=well_type_options,
                        #     #multi=True,
                        #     #value=list(WELL_TYPES.keys()),
                        #     className="dcc_control",
                        # ),
                        dcc.RadioItems(
                            id="whichavg",
                            options=whichAvgOPTS,
                            value="sevenday",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        dcc.RadioItems(
                            id="popratio",
                            options=popOPTS,
                            value="nonrelpop",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="projText"), html.P("Project:")],
                                    id="projnameyo",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="pstat"), html.P("Status:")],
                                    id="projstatus",
                                    className="mini_container",
                                ),
                                html.Div(
                                    [html.H6(id="pstate"), html.P("States in:")],
                                    id="states",
                                    className="mini_container",
                                ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("Other Info:")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-proj",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="projGraph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="cityGraph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        # html.Div(
        #     [
        #         html.Div(
        #             [dcc.Graph(id="pie_graph")],
        #             className="pretty_container seven columns",
        #         ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
        #     ],
        #     className="row flex-display",
        # ),
         # html.Div(children = [
         #    dcc.Markdown(id='hover-data',children = [""]),
         #    ], className='three columns'),
         # html.Div(children = [
         #    dcc.Markdown(children = [""],id = 'click-data')], className='three columns')
                  
                  
        ])



tab1=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose Country Specific Information:", className="control_label"),
                       dcc.Dropdown(
                            id="whichCountry",
                            #options=well_status_options,
                            options = countryOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'US',
                            className="dcc_control",
                        ),
                        #html.P("Choose Related City:", className="control_label"),
                        #dcc.Dropdown(
                        #    id="whichCity",
                            #options=well_type_options,
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                        #    className="dcc_control",
                        #),
                        dcc.RadioItems(
                            id="whichavgcountry",
                            options=whichAvgOPTS,
                            value="sevenday",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        dcc.RadioItems(
                            id="popratiocountry",
                            options=popOPTS,
                            value="nonrelpop",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-country",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.Div(
                                    [html.H6(id="countryText"), html.P("Country:")],
                                    id="countryName",
                                    className="mini_container",
                                ),
                                # html.Div(
                                #     [html.H6(id="countryStat"), html.P("Status:")],
                                #     id="countryStatus",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="countryStata"), html.P("Country Info:")],
                                #     id="countryStatus",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="countryOpen"), html.P("Opening Date:")],
                                #     id="open-date",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-country",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
               html.Div(
                    [html.Div(' ')],
                    className="row container-display",
                ),
                                
                html.Div(
                    [dcc.Graph(id="country_graph")],
                    className="pretty_container ten columns",
                ),
# =============================================================================
#                 html.Div(
#                     [dcc.Graph(id="cityGraph2")],
#                     className="pretty_container five columns",
#                 ),
# =============================================================================
            ],
            className="row flex-display",
        ),
# =============================================================================
#         html.Div(
#             [
#                 html.Div(
#                     [dcc.Graph(id="pie_graph2")],
#                     className="pretty_container seven columns",
#                 ),
#                 html.Div(
#                     [dcc.Graph(id="aggregate_graph")],
#                     className="pretty_container five columns",
#                 ),
#             ],
#             className="row flex-display",
#         )
# =============================================================================
        ])

tab2=html.Div([
    html.Div(
            [
                html.Div(
                    [

                        html.P("Choose State Specific Information:", className="control_label"),
                       dcc.Dropdown(
                            id="whichState",
                            #options=well_status_options,
                            options = stateOPTS,
                            #multi=True,
                            #value=list(WELL_STATUSES.keys()),
                            value = 'CO',
                            className="dcc_control",
                        ),
                        #html.P("Choose Related City:", className="control_label"),
                        #dcc.Dropdown(
                        #    id="whichCity",
                            #options=well_type_options,
                            #multi=True,
                            #value=list(WELL_TYPES.keys()),
                        #    className="dcc_control",
                        #),
                        dcc.RadioItems(
                            id="whichavgstate",
                            options=whichAvgOPTS,
                            value="sevenday",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control"
                            
                        ),
                        dcc.RadioItems(
                            id="popratiostate",
                            options=popOPTS,
                            value="nonrelpop",
                            labelStyle={"display": "inline-block"},
                            className="dcc_control",
                        ),
                        
                    ],
                    className="pretty_container four columns",
                    id="cross-filter-options-state",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                # html.Div(
                                #     [html.H6(id="well_text"), html.P("State:")],
                                #     id="stateName",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="gasText"), html.P("Status:")],
                                #     id="stateStatus",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="oilText"), html.P("")],
                                #     id="oil",
                                #     className="mini_container",
                                # ),
                                # html.Div(
                                #     [html.H6(id="waterText"), html.P("")],
                                #     id="water",
                                #     className="mini_container",
                                # ),
                            ],
                            id="info-container-state",
                            className="row container-display",
                        ),
                    ],
                    id="right-column",
                    className="eight columns",
                ),
            ],
            className="row flex-display",
        ),
        html.Div(
            [
                html.Div(
                    [dcc.Graph(id="state_graph")],
                    className="pretty_container seven columns",
                ),
                html.Div(
                    [dcc.Graph(id="statePredGraph")],
                    className="pretty_container five columns",
                ),
            ],
            className="row flex-display",
        ),
        # html.Div(
        #     [
        #         html.Div(
        #             [dcc.Graph(id="pie_graph2")],
        #             className="pretty_container seven columns",
        #         ),
        #         html.Div(
        #             [dcc.Graph(id="aggregate_graph")],
        #             className="pretty_container five columns",
        #         ),
        #     ],
        #     className="row flex-display",
        # )
        ])

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True,
                 meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server

app.layout = html.Div(
    [
        dcc.Store(id="aggregate_data"),
        html.Div(id="output-clientside"),
        html.Div(
            [
                html.Div(
                    [
                        #html.Img(
                        #    src = img,
                            #src='data:image/png;base64,{}'.format(encoded_image.decode()),
                        #    id="plotly-image",
                        #    style={
                        #        "height": "60px",
                        #        "width": "auto",
                        #        "margin-bottom": "25px",
                        #    },
                       # )
                    ],
                    className="one-third column",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Southern Cross Project-Specific Information",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "Coronavirus Impact", style={"margin-top": "0px"}
                                ),
                            ]
                        )
                    ],
                    className="one-half column",
                    id="title",
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                html.H3(
                                    "Last Updated",
                                    style={"margin-bottom": "0px"},
                                ),
                                html.H5(
                                    "6/2/20", style={"margin-top": "0px"}
                                ),
                              dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
                                  dcc.Tab(id="tab-1", label='Country', value='tab-1-example'),
                                  dcc.Tab(id="tab-2", label='State', value='tab-2-example'),
                                  dcc.Tab(id='tab-3',label='Project',value = 'tab-3-example')
                                  ])

                            ]
                        )
                    ],
                    className="one-third row",
                    id="title2",
                ),

                
            ],
            id="header",
            className="row flex-display",
            style={"margin-bottom": "25px"},
        ),
        html.Div(id='tabs-content-example',
             children = tab3),
        
    ],
    id="mainContainer",
    style={"display": "flex", "flex-direction": "column",'backgroundColor':'white'},
)


@app.callback(dash.dependencies.Output('tabs-content-example', 'children'),
             [dash.dependencies.Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1-example':
        return tab1
    elif tab == 'tab-2-example':
        return tab2
    elif tab == 'tab-3-example':
        return tab3



@app.callback( dash.dependencies.Output('whichCity', 'options'),
    [dash.dependencies.Input('whichProj', 'value')]
)
def update_city_dropdown(name):
    return fnameDict[name]

@app.callback(dash.dependencies.Output('state_graph', 'figure'),
              [dash.dependencies.Input('whichState', 'value')     ,
               dash.dependencies.Input('whichavgstate','value'),
               dash.dependencies.Input('popratiostate','value')
               ])

def update_state_fig(input_value,which_avg,pop_rat):
    df = stateLags[stateLags.StateAbr == input_value]
    
    if which_avg == 'sevenday':
        xvals = df.Date
        yvalDeaths = df.death_7
        yvalCases = df.mean_7
        title = 'Weekly Cases and Deaths, <br> ' + input_value
        yCaseTitle = "Weekly Cases"
        yDeathTitle = "Weekly Deaths"
    elif which_avg == 'threeday':
        xvals = df.Date
        yvalDeaths = df.death_3
        yvalCases = df.mean_3
        title = 'Three-Day Cases and Deaths, <br>' + input_value
        yCaseTitle = "Three-Day Cases"
        yDeathTitle = "Three-Day Deaths"
    elif which_avg == 'daily':
        xvals = df['Date']
        yvalDeaths = df.deaths_mnnz
        yvalCases = df['confirmed_infectionsnz']
        title = 'Daily Cases and Deaths, <br>' + str(input_value)
        yCaseTitle = "Daily Cases"
        yDeathTitle = "Daily Deaths"   
    elif which_avg == 'total':
        xvals = df.Date
        yvalDeaths = df.totDeaths
        yvalCases = df.totCases
        title = 'Total Cases and Deaths, <br>' + input_value
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
         ,
         legend_orientation="h"

     )
        

    data = [mean_data,death_data]
    

    return{
        'data':data,
        'layout': layout
        }


@app.callback(dash.dependencies.Output('statePredGraph', 'figure'),
              [dash.dependencies.Input('whichState', 'value')     ,
               dash.dependencies.Input('whichavgstate','value'),
               dash.dependencies.Input('popratiostate','value')
               ])

def update_state_fig2(input_value,which_avg,pop_rat):
    df = predInf[predInf.StateAbr == input_value]
    
   #xvals = df.Date
   # yvalDeaths = df.death_7
   # yvalCases = df.mean_7
   # yCaseTitle = "Weekly Cases"
   # yDeathTitle = "Weekly Deaths"
    
    # if pop_rat == 'relpop':
    #     yvalDeaths = (yvalDeaths/df.Population)*1e5
    #     yvalCases = (yvalCases/df.Population)*1e5
    #     #title = title + 'per 100k people'
    #     yCaseTitle = yCaseTitle + ' per 100k'
    #     yDeathTitle = yDeathTitle + ' per 100k'
    
    yup = df['est_infections_upper']
    ylow = df['est_infections_lower']
    y = df['est_infections_mean']
    title = 'Estimate of True Daily Cases, ' + input_value
    ytitle = 'Estimated Cases'    
    
    
    if pop_rat == 'relpop':
        yup = df['est_inf_upr_pop']
        ylow = df['est_inf_lwr_pop']
        y = df['est_inf_mn_pop']
        title = 'Estimated Cases, Per 100k People, <br>' + input_value
        ytitle = 'Estimated Cases, per 100k people'
        
    upper_bound = go.Scatter(
        name='Upper Bound',
        x=df['Date'],
        y = yup,
        mode='lines',
        marker=dict(color="#444"),
        line=dict(width=0),
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty')
    
    trace = go.Scatter(
        name='Estimate',
        x=df['Date'],
        y=y,
        mode='lines',
        line=dict(color='rgb(31, 119, 180)'),
        fillcolor='rgba(68, 68, 68, 0.3)',
        fill='tonexty')

    lower_bound = go.Scatter(
        name='Lower Bound',
        x=df['Date'],
        y= ylow,
        marker=dict(color="#444"),
        line=dict(width=0),
        mode='lines')
     # How do I integrate the layout?
         
    data = [lower_bound, trace, upper_bound]

    layout = go.Layout(
        yaxis=dict(title=ytitle),
        title=title,
        showlegend = True,
        legend_orientation="h"
)
                

    return{
        'data':data,
        'layout': layout
        }



@app.callback(dash.dependencies.Output('projGraph','figure'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_project(whichProj):
    if whichProj == "ConEd":
        lat = 41.6
        lon = -73.7
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Con Edison"
        states = ["New York"]

    elif whichProj == "DukeOH":
        lat = 39.19
        lon = -84.5
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        states = ['Ohio', 'Kentucky','Indiana']
        title = "Duke (Ohio)"

    elif whichProj == "DomQuest":
        lat = 40.66
        lon = -111.9
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Dom Questar"
        states = ['Utah']

    elif whichProj == "WEC_WI":
        lat = 43
        lon = -87.9
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "WEC (WI)"
        states = ['Wisconsin']

    elif whichProj == "WPS_WI":
        lat = 43
        lon = -87.9
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "WPS (WI)"
        states = ['Wisconsin']

    elif whichProj == "PeoplesIL":
        lat = 41.84
        lon = -87.8
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Con Edison"
        states = ['Illinois',"Wisconsin","Indiana"]

    elif whichProj == "Aclara":
        lat = 41.6
        lon = -73.7
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "ACLARA"
        states = ["New York"]

    elif whichProj == "DukeIPI":
        lat = 39.19
        lon = -84.5
        zoom = 7
        lowlat = 36.5
        uplat = 42
        lowlon = -85
        uplon = -83 
        lat = 39.19
        lon = -84.5
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        states = ['Ohio', 'Kentucky','Indiana']
        title = "Duke (IPI)"

    elif whichProj == "norwhich":
        lat = 41.5
        lon = -72
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Norwich"
        states = ["Connecticut","Rhode Island"]

    elif whichProj == "Trussville":
        lat = 33.7
        lon = -86.9
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Trussville"
        states = ['Alabama']

    elif whichProj == "CPS_TX":
        lat = 32.76
        lon = -96.7
        zoom = 6
        lowlat = 32.7
        uplat = 34.4
        lowlon = -88
        uplon = -86
        zoom = 7
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "CPS, Texas"
        states = ['Texas']

    elif whichProj == "DominionSC":
        lat = 34
        lon = -80.9
        zoom = 6
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Dominion, SC"
        states = ['South Carolina']

    elif whichProj == "DominionNC":
        lat = 35.79
        lon = -80.2
        zoom = 5.6
        lowlat = -200
        uplat = 200
        lowlon = -200
        uplon = 200
        title = "Dominion, NC"
        states = ['North Carolina']
    
    
    usedat = citInfo[citInfo.Province_State.isin(states)]
    usedat = usedat[usedat.Lat<uplat]
    usedat = usedat[usedat.Lat>lowlat]
    usedat = usedat[usedat.Long_>lowlon]
    usedat = usedat[usedat.Long_<uplon]
    usedat['Date']= pd.to_datetime(usedat['Date']).astype(str)
    

    fig = px.scatter_mapbox(
        usedat,
        lat = 'Lat',
        lon = 'Long_',
        color = 'DailyNew',
        size = 'Confirmed',
        #color_continuous_scale=px.colors.sequential.Oranges, 
        size_max = 25,
        zoom = zoom,
        animation_frame = 'Date',
        animation_group = 'Combined_Key',
        hover_name = 'Combined_Key',
        hover_data = {'DailyNew'}
        )
    fig.update_layout(
        autosize=False,
        width=800,
        height=800,
        title_text=title,
        mapbox=dict(
           # accesstoken=mapbox_access_token,
           # bearing=0,
            center=go.layout.mapbox.Center(
                lat=lat,
                lon=lon
            )
        ),
        legend_orientation="h",
        )
    fig.update()

    return fig


@app.callback(dash.dependencies.Output('projnameyo', 'children'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_textyo(whichproj):
    nam = file[file.Project==whichproj].iloc[0]['Name']       
    return "Project Name: " + nam 
 
    
@app.callback(dash.dependencies.Output('countryName', 'children'),
              [dash.dependencies.Input('whichCountry','value')]             
              )
def update_ct(whichcountry):
    return "Country: " + str(whichcountry)
 
    
 
@app.callback(dash.dependencies.Output('projstatus', 'children'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_text2(whichproj):
    stat = file[file.Project==whichproj].iloc[0]['Status']       
    return "Project Status: " + stat 

@app.callback(dash.dependencies.Output('states', 'children'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_text55(whichproj):
    statez = file[file.Project==whichproj].iloc[0]['States']       
    return "States the project is in: " + statez


@app.callback(dash.dependencies.Output('business', 'children'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_text56(whichproj):
    biz = file[file.Project==whichproj].iloc[0]['States']       
    return "Business the project does:  " + biz



@app.callback(dash.dependencies.Output('open-date', 'children'),
              [dash.dependencies.Input('whichProj','value')]             
              )
def update_text4(whichproj):
    stat = file[file.Project==whichproj].iloc[0]['openDate']       
    return "Opening Date:" + stat 




    
@app.callback(dash.dependencies.Output('country_graph', 'figure'),
              [dash.dependencies.Input('whichCountry', 'value'),
               dash.dependencies.Input('whichavgcountry','value'),
               dash.dependencies.Input('popratiocountry','value')
               ])

def update_country_fig(input_value,which_avg,pop_rat):
    df = countryLags[countryLags.Country_Region == input_value]
    xvalsCases = df.Date
    xvalsDeaths = df.Date
    if input_value == 'US':
        df = usLagOverall
        df2 = countryLags[countryLags.Country_Region == input_value]
        xvalsCases = df.Date
        xvalsDeaths = df2.Date
    if which_avg == 'sevenday':
        yvalDeaths = df.death_7
        if input_value == 'US':
            yvalDeaths = df2.death_7
        yvalCases = df.mean_7
        title = 'Weekly Cases and Deaths, <br>' + input_value
        yCaseTitle = "Weekly Cases"
        yDeathTitle = "Weekly Deaths"
    elif which_avg == 'threeday':
        yvalDeaths = df.death_3
        if input_value == 'US':
            yvalDeaths = df2.death_3
        yvalCases = df.mean_3
        title = 'Three-Day Cases and Deaths, <br>' + input_value
        yCaseTitle = "Three-Day Cases"
        yDeathTitle = "Three-Day Deaths"
    elif which_avg == 'daily':
        if input_value == "US":
            yvalDeaths = df2.newDeath
            yvalCases = df.confirmed_infectionsnz
        elif input_value != "US":
            yvalDeaths = df.newDeath
            yvalCases = df.newConfirmed            
        title = 'Daily Cases and Deaths, <br>' + input_value
        yCaseTitle = "Daily Cases"
        yDeathTitle = "Daily Deaths"   
    elif which_avg == 'total':
        if input_value == "US":
            yvalDeaths = df2.DeathCountry
            yvalCases = df.totCases
        elif which_avg != "US":
            yvalDeaths = df.DeathCountry
            yvalCases = df.ConfirmedCountry
        title = 'Total Cases and Deaths, <br>' + input_value
        yCaseTitle = "Total Cases"
        yDeathTitle = "Total Deaths"
    if pop_rat == 'relpop':
        pop = df.Population[0]
        if input_value == "Italy":
            pop = 60.36e6
        
        yvalDeaths = (yvalDeaths/pop)*1e5
        yvalCases = (yvalCases/pop)*1e5
        #title = title + 'per 100k people'
        yCaseTitle = yCaseTitle + ' per 100k'
        yDeathTitle = yDeathTitle + ' per 100k'

    
        
    # Create traces
    death_data = go.Scatter(
         x= xvalsDeaths,
         y= yvalDeaths,
         name='Deaths',
         yaxis = 'y2'
     )
    mean_data = go.Scatter(
         x=xvalsCases,
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
         ),
         legend_orientation="h",

     )
       
    data = [mean_data,death_data]

    return{
        'data':data,
        'layout': layout
        }

@app.callback(
    dash.dependencies.Output('hover-data', 'children'),
    [dash.dependencies.Input('projGraph', 'hoverData')])
def display_hover_data(hoverData):
    #return json.dumps(hoverData, indent=2)
    return hoverData['points'][0]['id']


@app.callback(
    dash.dependencies.Output('click-data', 'children'),
    [dash.dependencies.Input('projGraph', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)




    
@app.callback(dash.dependencies.Output('cityGraph','figure'),
              [dash.dependencies.Input('projGraph','hoverData'),
               dash.dependencies.Input('whichavg','value'),
               dash.dependencies.Input('popratio', 'value')
               ]             
              )

def update_city_fig2(input_value2,which_avg,pop_rat):
    input_value = input_value2['points'][0]['id']
    df = citLags[citLags.Combined_Key == input_value]
    
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
        yvalDeaths = df.Deaths
        yvalCases = df.Confirmed
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
             title=yCaseTitle,
             range = [0,yvalCases.max()]
         ),
         yaxis2=dict(
             title=yDeathTitle,
             overlaying='y',
             side='right',
             range = [0,yvalDeaths.max()]
         ),
         legend_orientation="h",

         
     )
       
    data = [mean_data,death_data]

    return{
        'data':data,
        'layout': layout
        }

# =============================================================================
# 
# @app.callback(dash.dependencies.Output('cityGraph','figure'),
#               [dash.dependencies.Input('whichCity','value'),
#                dash.dependencies.Input('whichavg','value'),
#                dash.dependencies.Input('popratio', 'value')
#         
#                ]             
#               )
# 
# def update_city_fig(input_value,which_avg,pop_rat):
#     df = citLags[citLags.Combined_Key == input_value]
#     
#     if which_avg == 'sevenday':
#         xvals = df.Date
#         yvalDeaths = df.death_7
#         yvalCases = df.mean_7
#         title = 'Weekly Cases and Deaths, ' + input_value
#         yCaseTitle = "Weekly Cases"
#         yDeathTitle = "Weekly Deaths"
#     elif which_avg == 'threeday':
#         xvals = df.Date
#         yvalDeaths = df.death_3
#         yvalCases = df.mean_3
#         title = 'Three-Day Cases and Deaths, ' + input_value
#         yCaseTitle = "Three-Day Cases"
#         yDeathTitle = "Three-Day Deaths"
#     elif which_avg == 'daily':
#         xvals = df.Date
#         yvalDeaths = df.newDeath
#         yvalCases = df.newConfirmed
#         title = 'Daily Cases and Deaths, ' + input_value
#         yCaseTitle = "Daily Cases"
#         yDeathTitle = "Daily Deaths"   
#     elif which_avg == 'total':
#         xvals = df.Date
#         yvalDeaths = df.Deaths
#         yvalCases = df.Confirmed
#         title = 'Total Cases and Deaths, ' + input_value
#         yCaseTitle = "Total Cases"
#         yDeathTitle = "Total Deaths"
#     if pop_rat == 'relpop':
#         yvalDeaths = (yvalDeaths/df.Population)*1e5
#         yvalCases = (yvalCases/df.Population)*1e5
#         #title = title + 'per 100k people'
#         yCaseTitle = yCaseTitle + ' per 100k'
#         yDeathTitle = yDeathTitle + ' per 100k'
#     
#     
#         
#     # Create traces
#     death_data = go.Scatter(
#          x= xvals,
#          y= yvalDeaths,
#          name='Deaths',
#          yaxis = 'y2'
#      )
#     mean_data = go.Scatter(
#          x=xvals,
#          y=yvalCases,
#          name='Cases'
#          # yaxis='y2'
#      )
#      # How do I integrate the layout?
#     layout = go.Layout(
#          title=title,
#          yaxis=dict(
#              title=yCaseTitle,
#              range = [0,yvalCases.max()]
#          ),
#          yaxis2=dict(
#              title=yDeathTitle,
#              overlaying='y',
#              side='right',
#              range = [0,yvalDeaths.max()]
#          ),
#          legend_orientation="h",
# 
#          
#      )
#        
#     data = [mean_data,death_data]
# 
#     return{
#         'data':data,
#         'layout': layout
#         }
# 
# 
# =============================================================================

if __name__ == '__main__':
    app.run_server(debug=False)
