from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class FarmPolygons(Document):
    """Auto-generated MongoDB collection: FarmPolygons"""
    meta = {'collection': 'farmpolygons'}
    id = ObjectIdField(primary_key=True)
    farm_id = ObjectIdField(primary_key=True)
    geojson = StringField()
    latitude = StringField()
    longitud = StringField()
    animals_amount = StringField()
    buffer_size = StringField()
    field_capacity = StringField()