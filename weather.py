import requests

place_list = [(62.0397, 129.7422, 'Yakutsk'), (63.7467, 68.5170, 'Iqaluit'),
              (45.8038, 126.5350, 'Harbin'), (51.1605, 71.4704, 'Astana'),
              (54.9833, 82.8964, 'Novosibirsk'), (71.1667, -39.9333,
                                                  'Eismitte'),
              (39.9450, 105.8172, 'Fraser'), (64.2823, 135.0000, 'Yukon'),
              (71.2906, 156.7886, 'Barrow'), (45.4215, 75.6972, 'Ottawa')]


class Place:
    def __init__(self, lat, lon, name):
        self.lat = lat
        self.lon = lon
        self.name = name

    def __str__(self):
        return (f'{self.name} latitude:{self.lat} longitude:{self.lon}')


def buildPlace(list):
    places = []
    for city in list:
        place = Place(city[0], city[1], city[2])
        places.append(place)
    return places


places = buildPlace(place_list)


def get_Weather(lat, lon):
    url = 'https://api.climacell.co/v3/weather/realtime'
    payload = {
        "apikey": "ekQTVNXcywUsz7LDWg7w9fGwNl87yCl2",
        "lat": Place.lat,
        "lon": Place.lon,
        "fields": ["temp", "precipitation", "wind_gust"],
        "unit_system": "us",
    }
