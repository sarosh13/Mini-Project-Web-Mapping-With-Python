# Project-1-Web-Mapping-With-Python

- Marker shows the elevation of volcanoes.
- Colour of the countries shows the population range.
    
    Below 1 crore it is in 'Green'
    Between 1 crore & 2 crore is in 'Orange'
    Above 2 crore is in 'Red'

![image](https://user-images.githubusercontent.com/87830353/178113165-12afcf53-94e7-4490-996d-08a603127973.png)
    
    
# Summary:
 
 Volcanoes:
 1. This project contain two data files i.e volcanoes.txt & world.json.
 2. Read the volcanoes file using Python library pandas and implemented operations on it.
 3. Imported folium module to visualize geospatial data.
 4. Created base map of world using folium.
 5. After Traversing through files, applied markers on the map using folium module.
 6. Added link on name of each volcano or marker using HTML. 
 
 Population:
 1. world.json file contains the information regarding population, countries, regions, etc.
 2. With the help of folium function GeoJson, read world.json file and implemented style function on each country using lambda function.
 3. If population falls down below 1 crore then display it as 'green'.
 4. If population falls between below 1-2 crore then display it as 'orange'.
 5. If population goes above 2 crore then display it as 'red'.

