import sys
import json
import urllib.request as urllib2
import pandas as pd

pd.set_option('display.max_rows', 300)
pd.set_option('display.max_columns', 8)
pd.set_option('display.width', 200)


data = urllib2.urlopen('https://data.buienradar.nl/2.0/feed/json')
data = json.loads(data.read())
#temp = [40]
#a = 1


df = pd.DataFrame(data["actual"]["stationmeasurements"],columns=['stationname','temperature','humidity','weatherdescription'])
df['temperature'] = df['temperature'].fillna(0)
df['humidity'] = df['humidity'].fillna(0)

print(df)

df2 = pd.DataFrame(data["forecast"]["fivedayforecast"],columns=['day','rainChance','mmRainMax','weatherdescription'])
print(df2)


             # "C°

        
