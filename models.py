class Offer:

    def __init__(self, title: str, location: str, price: float, rooms: int,
                 area: float, link: str, currency='PLN', area_unit='m2'):
        self.title = title
        self.location = location
        self.price = price
        self.rooms = rooms
        self.area = area
        self.link = link
        self.currency = currency
        self.area_unit = area_unit

    def __str__(self):
        return f'''\
Title: {self.title}
Location: {self.location}
Price: {self.price} {self.currency}
Rooms: {self.rooms}
Area: {self.area} {self.area_unit}
Link: {self.link}
        '''
