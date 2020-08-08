import sys
import json
import urllib.request as urllib2

data = urllib2.urlopen('https://data.buienradar.nl/2.0/feed/json',data=None)
data = json.loads(data.read())
temp = [40]
a = 1


for i in data["actual"]["stationmeasurements"]:
    
       
        if 'temperature' in i:
            temp = str(i["temperature"])
        else:
            temp = " - "
             
        print( temp + "C° - " + i["stationname"] )
        
print("")
print("5 dagen voorspelligen")
print("")

for i in data["forecast"]["fivedayforecast"]:
        
        print(i["day"] + " regen " + str(i["rainChance"]) + " %" + " - " + str(i["mmRainMax"]) + "mm" + " - " + i["weatherdescription"] )
    
    
 
        
