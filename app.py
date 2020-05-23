import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

##### import dataframe
file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/countryLags.csv'
countryLags = pd.read_csv(file_name)
countryLags['Date'] = countryLags['Date'].astype('datetime64[ns]')

file_name = 'https://raw.githubusercontent.com/elimywilliams/sc_covid19/master/allStateLags.csv'
stateLags = pd.read_csv(file_name)
stateLags['Date'] = stateLags['datetest'].astype('datetime64[ns]')

######
px.set_mapbox_access_token('pk.eyJ1IjoiZXdpbGxpYW1zMjAyMCIsImEiOiJja2FpdTIxOXMwM2wzMnFtbmVmb3IzZDJ6In0.TVsQ-iu8bN4PQLkBCr6tQQ')
#######
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
################





########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='lightblue'
color2='darkgreen'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Flying Dog Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=False)
