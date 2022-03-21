
from . import db
import enum
from datetime import date

class PropertyType(enum.Enum):
    House = 'House'
    Appartment  = 'Apartment'
    Cottage = 'Cottage'
    

class Property(db.Model):
    __tablename__ = 'homes'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title',db.String(80))
    description = db.Column('Description',db.String(2355))
    rooms = db.Column('No. of Rooms',db.String(3)) 
    bathrooms = db.Column('No. of Bathrooms',db.String(3))
    price = db.Column('Price',db.String(12))
    property_type = db.Column('Property Type',db.String(9))
    location = db.Column('Location',db.String(80))
    photo_name = db.Column('Photo Name',db.String(80))

    def __init__(self, title, description, rooms, bathrooms, price, propertyType, location, photo_name):
        self.title = title
        self.description = description
        self.rooms = rooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = propertyType
        self.location = location
        self.photo_name = photo_name
