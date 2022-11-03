#REV B
from geojson import Point, Feature, FeatureCollection, dump                                                                                 #geojson helps put data in a geojson format
import pyodbc                                                                                                                               #grabs info fromSQL SERVER

features = []                                                                                                                               #empty array for storing feature collection
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-I9NFHPFQ;'
                      'Database=AVYDATA3;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("""select * from avydata3
	where latitude is not null										
	AND
	cast(latitude as decimal) > 37
	AND
	area = 'Salt Lake';""")


date = ""                                                                                                                      #Giving important items in row tuple alias.
reg = ""                                                                                                                         #this assumes select * from my data base
zone = ""                                                                                                                          #aliases can be remaped to different...
whotrig = ""                                                                                                                        #column numbers below or SQL query can...
trignote = ""                                                                                                                       #be re-ordered to match aliases.
prob = ""                                                                                                                           #some aliases will be reformated here
depth = ""                                                                                                                          #these aliases will be renewed each iteration                                                                                                                    
width = ""
length = ""
aspect = ""
elevation = ""
carried = ""
caught = ""
partb = ""
fullb = ""
deaths = ""
lat = 0
long = 0


def symbol():                                                                                                                                #determines the icon for the map
    if deaths is not None and int(deaths) > 0:                                                                                                                     #... row is filled in main loop and called in this functions
        return "Danger"                                                                                                                     #if anyone dies return "danger" (skull and xbones)
    elif prob == "facets" or prob == "Facets" or prob == "Depth Hoar" or prob == "Surface Hoar":                                         #other than that, match avy problem with...
        return "https://www.avalanches.org/wp-content/uploads/2019/03/Icon-Avalanche-Problems-Persistent-weak-Layer-c-EAWS.jpg"             #...descriptive symbol from web
    elif prob == "New Snow/Old Snow Interface" or prob == "New Snow":
        return "https://www.avalanches.org/wp-content/uploads/2019/03/Icon-Avalanche-Problems-New-Snow-c-EAWS.jpg"
    elif prob == "Wet Grains" or prob == "Wet grains" or prob == "wet grains":
        return "https://www.avalanches.org/wp-content/uploads/2019/03/Icon-Avalanche-Problems-Wet-snow-c-EAWS.jpg"
    else:
        return "https://cdn1.sbnation.com/imported_assets/742161/31hvRp-xSeL._SL500_AA300_.jpg?_ga=2.200505198.1191482502.1666137235-1375161525.1666137235"

def comments():

    if date is not None:
        datecomment = " on {}" .format(date) 
    else:
        datecomment  = "on unknown date"

               
    if zone is not None:
        zonecomment = " in the {} area. " .format(zone)
    else:
        zonecomment = "."

    if whotrig is not None and whotrig != "Natural" and whotrig != "Unknown":
        trigcomment = "The trigger was a {}." .format(whotrig)
    elif whotrig is not None:
        trigcomment = "The trigger was {}." .format(whotrig)
    else:
        trigcomment = "The trigger was unknown."

    if depth is not None:
        depthcomment = "\nDepth = {}" .format(depth)
    else:
        depthcomment = ""

    if width is not None:
        widthcomment = "\nWidth = {}" .format(width)
    else:
        widthcomment = ""

    if length is not None:
        lengthcomment = "\nLength = {}" .format(length)
    else:
        lengthcomment = "" 

    return "This avalanche occured " datecomment, zonecomment, "\n", trigcomment, depthcomment, widthcomment, lengthcomment

def folder(): #insert folder name
    return "test folder 1"

############################################################ MAIN FOR LOOP

for i in cursor:
    row = cursor.fetchone()                                                                                                                 #fetch current row and store in row tuple                                                                                                                               
                                                                                                                                                                                                                                                                  
    date = str(row[0])                                                                                                                      #Giving important items in row tuple alias.
    reg = row[1]                                                                                                                            #this assumes select * from my data base
    zone = row[2]                                                                                                                           #aliases can be remaped to different...
    whotrig = row[3]                                                                                                                        #column numbers below or SQL query can...
    trignote = row[4]                                                                                                                       #be re-ordered to match aliases.
    prob = row[5]                                                                                                                           #some aliases will be reformated here
    depth = row[6]                                                                                                                          #these aliases will be renewed each iteration                                                                                                                    
    width = row[7]
    length = row[8]
    aspect = row[9]
    elevation = row[10]
    carried = row[12]
    caught = row[13]
    partb = row[14]
    fullb = row[15]
    deaths = row[17]
    lat = float(row[18])
    long = float(row[19])

    coords = long, lat                                                                                                                      #geojson wants long then lat opposite of common format
    point = Point(coords)

    
    features.append(Feature(geometry=point, properties={"marker-symbol":symbol(),"description":comments(),"title":zone,"marker-size":"0.75","class":"Marker","folderId":folder()}))     #check on null color
    feature_collection = FeatureCollection(features)
########################################################### END MAIN LOOP


with open('C:/Users/cameron/Downloads/map.geojson', 'w') as f:
	dump(feature_collection, f)
