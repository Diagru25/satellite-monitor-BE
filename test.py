# x = -0.00008233142526670038
# print('%.2E' % x)
import geopy.geocoders
from geopy.geocoders import Nominatim
from geopy.point import Point
from deep_translator import GoogleTranslator
geopy.geocoders.options.default_timeout = 7
locator = Nominatim(user_agent='myGeocoder')
print(locator.timeout)
lat = -10.673104
long = 24.022580
coor = (Point(lat,long))
location = locator.reverse(coor)
print(location)
location_vi = GoogleTranslator(source='auto', target='vi').translate(location.address)
print(location_vi)