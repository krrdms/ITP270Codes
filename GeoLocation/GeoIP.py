import requests

def display_ip():
    """  Function To Print GeoLocation Latitude & Longitude """
    ip_request = requests.get('https://get.geojs.io/v1/ip.json')
    my_ip = ip_request.json()['ip']
    geo_request = requests.get('https://get.geojs.io/v1/ip/geo/' +my_ip + '.json')
    geo_data = geo_request.json()
    print({'latitude': geo_data['latitude'], 'longitude': geo_data['longitude']})
    print({'city': geo_data['city'], 'region': geo_data['region'], 'country': geo_data['country']})

if __name__ == '__main__':
    display_ip()