from models import Geoposition
from rest_framework.serializers import ModelSerializer, ValidationError
import requests

class GeopositionSerializer(ModelSerializer):
    class Meta:
        model = Geoposition
        fields = ['id', 'address','latitude','longitude','elevation']
        read_only_fields = ('latitude','longitude','elevation')
    def create(self, data):
        raw_address = data['address']
        #do stuff to set the address and stuff
        rawResult = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+raw_address+'&key=AIzaSyC2xkjidXO_m2qfAXLey1xUlOdXFs3Kgig')
        result = rawResult.json()
        if result['status'] == 'OK':
            current_result = result['results'][0]
            lat = current_result['geometry']['location']['lat']
            lng = current_result['geometry']['location']['lng']
            address = current_result['formatted_address']

            rawResult = requests.get('https://maps.googleapis.com/maps/api/elevation/json?locations=' + str(lat) + ',' + str(lng) + '&key=AIzaSyBCQhLyh6QuFQ8s4atlthsX7PXwZWOkV84')
            elevation = rawResult.json()['results'][0]['elevation']
            geo = Geoposition(
                address = address,
                latitude = lat,
                longitude = lng,
                elevation = elevation
            )
            geo.save()
            return geo

        raise ValidationError('Address not found')
