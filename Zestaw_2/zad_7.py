import requests


class Brewery:
    def __init__(self, id, name, brewery_type, address_1, address_2, address_3, city, state_province, postal_code,
                 country, longitude, latitude, phone, website_url, state, street):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.address_1 = address_1
        self.address_2 = address_2
        self.address_3 = address_3
        self.city = city
        self.state_province = state_province
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.phone = phone
        self.website_url = website_url
        self.state = state
        self.street = street

    def __str__(self):
        return (f"Brewery:\n\tID: {self.id}\n\tName: {self.name}\n\tBrewery Type: {self.brewery_type}\n\t"
                f"Address 1: {self.address_1}\n\tAddress 2: {self.address_2}\n\tAddress 3: {self.address_3}\n\t"
                f"City: {self.city}\n\tState Province: {self.state}\n\tPostal Code: {self.postal_code}\n\t"
                f"Country: {self.country}\n\tLongitude: {self.longitude}\n\tLatitude: {self.latitude}\n\t"
                f"Phone: {self.phone}\n\tWebsite URL: {self.website_url}\n\tState: {self.state}\n\t"
                f"Street: {self.street}")


brews = []

api_taker = requests.get("https://api.openbrewerydb.org/v1/breweries?per_page=20").json()

for item in api_taker:
    brew = Brewery(item['id'], item['name'], item['brewery_type'], item['address_1'], item['address_2'],
                   item['address_3'], item['city'], item['state_province'], item['postal_code'], item['country'],
                   item['longitude'], item['latitude'], item['phone'], item['website_url'], item['state'], item['street'])
    brews.append(brew)

for brew in brews:
    print(brew)
