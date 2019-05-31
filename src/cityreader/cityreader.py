# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City():
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []

def cityreader(cities=[]):
  import csv
  with open('cities.csv') as c_csv:
    c_contents = csv.reader(c_csv, delimiter=',')
    line = 0
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    for row in c_contents:
      # skip the first row of headers
      if line == 0:
        line += 1
      # append data from consequent rows
      else:
        cities.append(City(row[0], row[3], row[4]))
        line += 1
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line
for c in cities:
    print(c.name, c.lat, c.lon)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # go through each city and check if its lat/lon fall within the coordinates
  # within will hold the cities that fall within the specified region
  within = [f"{city.name}: ({city.lat},{city.lon})" for city in cities if (lat2 <= float(city.lat) <= lat1) and (lon2 <= float(city.lon) <= lon1)]
  return within

co_1 = str(input("Enter lat1,lon1: ")).split(',')
co_2 = str(input("Enter lat2,lon2: ")).split(',')

# assign varibles to each coordinate
lat_1 = float(co_1[0])
lon_1 = float(co_1[1])
lat_2 = float(co_2[0])
lon_2 = float(co_2[1])

# reorder city_reader stretch call, passing the 'biggest' coordinate set first
if lat_1 > lat_2:
  print(cityreader_stretch(lat_1, lon_1, lat_2, lon_2, cities))
else:
  print(cityreader_stretch(lat_2, lon_2, lat_1, lon_1, cities))
