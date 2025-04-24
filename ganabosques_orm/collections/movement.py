from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.sourcemovement import SourceMovement

class Movement(Document):
    """Auto-generated MongoDB collection: Movement"""
    meta = {'collection': 'movement'}
    id = ObjectIdField(primary_key=True)
    date = DateTimeField()
    type_origin = StringField()
    type_destination = StringField()
    source = EmbeddedDocumentField(SourceMovement)
    ext_id = StringField()
    farm_id_origin = ObjectIdField(primary_key=True)
    farm_id_destination = ObjectIdField(primary_key=True)
    enterprise_id_origin = ObjectIdField(primary_key=True)
    enterprise_id_destination = ObjectIdField(primary_key=True)
    movement = StringField()
    species = StringField()