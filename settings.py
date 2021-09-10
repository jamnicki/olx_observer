# SCRAPING
BASE_URL = 'https://www.otodom.pl'
OFFERS_URL = 'https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/wroclaw?roomsNumber=%5BTHREE%2CFOUR%5D&priceMax=3300&distanceRadius=0&market=ALL&page=1&limit=24&by=LATEST&direction=DESC&locations[0][regionId]=1&locations[0][cityId]=39&locations[0][subregionId]=381'  # noqa: E501
LOCATION_TAG_CLASS = 'css-17o293g es62z2j23'
PRICE_TAG_CLASS = 'css-lk61n3 es62z2j20'
DETAILS_TAG_CLASS = 'css-xlgkh5 es62z2j22'

# SMTP
SMTP_HOST = 'smtp.gmail.com'
SMTP_PORT = 587
RECEIVERS = [
    'mail1@domain.com',
    'mail2@domain.com',
    'mail3@domain.com'
]
