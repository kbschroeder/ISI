import plotly as py
import plotly.graph_objs as go
import pandas as pd

mapbox_access_token = 'pk.eyJ1Ijoia2JzY2hyb2VkZXI0MiIsImEiOiJjangzbGNpb3MwMDlzNGFydWY0eDA2ajZqIn0.8bveXwKl2lQBwh0bsatE8A'

df = pd.read_csv('dateBirthCleaned.csv')

birth_lat = df['Lat']
birth_lon = df['Lon']

df['placeBirthLabel'] = df['placeBirthLabel'].apply(lambda x: x.capitalize())
birth_city = df.groupby('placeBirthLabel').agg('count')['occupationLabel']

data = [go.Scattermapbox(lat=birth_lat, lon=birth_lon,
                         mode='markers',
                         marker=dict(
                                    #size = birth_city,
                                    size = 4,
                                    opacity=0.05,
                                    color=birth_city,
                                    #colorbar=dict(title=''),
                                    colorscale='Jet'),
                         #text=df['yearBirth']
                                     )]

layout = go.Layout(title='Locations of Baseball Players Births',
                   autosize=True,
                   hovermode='closest',
                   showlegend=False,
                   mapbox=dict(accesstoken=mapbox_access_token,
                               bearing=0,
                               center=dict(lat=39.82, lon=-98.57),
                               pitch=0,
                               zoom=3,
                               style='light'))


fig = dict(data = data, layout = layout)
py.offline.plot(fig)