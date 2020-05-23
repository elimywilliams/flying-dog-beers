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
       
    data = [mean_data,death_data]

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
        
        
 
  
   data = [mean_data,death_data]
    
    return{
        'data':data,
        'layout': layout
        }

if __name__ == '__main__':
    app.run_server(debug=False)
