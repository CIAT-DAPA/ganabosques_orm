from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.attributes import Attributes

class FarmRisk(Document):
    """Auto-generated MongoDB collection: FarmRisk"""
    meta = {'collection': 'farmrisk'}
    id = ObjectIdField(primary_key=True)
    farm_id = ObjectIdField(primary_key=True)
    farm_polygons_id = ObjectIdField(primary_key=True)
    deforestation = EmbeddedDocumentField(Attributes)
    protected = EmbeddedDocumentField(Attributes)
    risk_direct = StringField()
    risk_input = StringField()
    risk_output = StringField()
    risk_total = StringField()