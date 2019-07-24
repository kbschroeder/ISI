import requests
import pandas as pd
from collections import OrderedDict
import csv

url = 'https://query.wikidata.org/sparql'
query = """
SELECT ?occupation ?occupationLabel WHERE {
  ?occupation wdt:P106 wd:Q10871364.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en". }
}


"""
r = requests.get(url, params={'query': query, 'format': 'json'})
data = r.json()

occupation = []
for item in data['results']['bindings']:
    occupation.append(OrderedDict({
        'name': item['occupation']['value'],
        'nameLabel': item['occupationLabel']['value']}))

df = pd.DataFrame(occupation)
df.set_index('name', inplace=True)
# df = df.astype({'baseballReferenceMajorLeagueID': float, 'dateBirth': float})
df.head()

#export_csv = df.to_csv(r'C:\User\Kate\Desktop\WikidataNames.csv')

print(df)

df.to_csv(r'WikidataNames.csv')

