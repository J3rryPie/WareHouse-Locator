from .models import City
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def Lat_Lon():
    geolocator = Nominatim(user_agent='user')
    cities=City.objects.all()
    for i in cities:
        destination=geolocator.geocode(i.name,addressdetails=True)
        i.x_coordinate=destination.raw['lat']
        i.y_coordinate=destination.raw['lon']
        i.save()

def calc_weights():
    cities=City.objects.all()
    n=cities.count()
    weights=[]
    for i in cities:
            l1=[]
            for j in cities:
                point1=(i.x_coordinate,i.y_coordinate)
                point2=(j.x_coordinate,j.y_coordinate)
                l1.append(round(geodesic(point1,point2).km,2))
            weights.append(l1)
    return weights

def get_center_coordinates(latA,lonA,latB,lonB):
    cord=[(latA+latB)/2,(lonA+lonB)/2]
    return cord