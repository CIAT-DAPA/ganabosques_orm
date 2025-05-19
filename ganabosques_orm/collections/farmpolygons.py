from mongoengine import Document, StringField, ObjectIdField, ReferenceField, FloatField, IntField
from ganabosques_orm.collections.farm import Farm

class FarmPolygons(Document):
    """Auto-generated MongoDB collection: FarmPolygons"""
    meta = {'collection': 'farmpolygons'}
    farm_id = ReferenceField(Farm)
    geojson = StringField()
    latitude = FloatField()
    longitud = FloatField()
    animals_amount = IntField()
    buffer_size = FloatField()
    field_capacity = FloatField()