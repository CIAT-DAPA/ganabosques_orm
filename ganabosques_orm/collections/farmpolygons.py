from mongoengine import Document, StringField, ReferenceField, FloatField, IntField, EmbeddedDocumentField
from ganabosques_orm.collections.farm import Farm
from ganabosques_orm.auxiliaries.bufferpolygon import BufferPolygon

class FarmPolygons(Document):
    """Auto-generated MongoDB collection: FarmPolygons"""
    meta = {'collection': 'farmpolygons'}
    farm_id = ReferenceField(Farm)
    geojson = StringField()
    latitude = FloatField()
    longitud = FloatField()
    farm_ha = FloatField()
    radio = FloatField()
    buffer_inputs = EmbeddedDocumentField(BufferPolygon)