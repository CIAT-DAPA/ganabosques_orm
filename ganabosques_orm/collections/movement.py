from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField
from typing import Optional
from ganabosques_orm.enums.typemovement import TypeMovement
from ganabosques_orm.auxiliaries.sourcemovement import SourceMovement
from ganabosques_orm.auxiliaries.classification import Classification

class Movement(Document):
    """Auto-generated MongoDB collection: Movement"""
    meta = {'collection': 'movement'}
    id = ObjectIdField(primary_key=True)
    date = DateTimeField()
    type_origin = EnumField(TypeMovement)
    type_destination = EnumField(TypeMovement)
    source = EmbeddedDocumentField(SourceMovement)
    ext_id = StringField()
    farm_id_origin = ObjectIdField(primary_key=True)
    farm_id_destination = ObjectIdField(primary_key=True)
    enterprise_id_origin = ObjectIdField(primary_key=True)
    enterprise_id_destination = ObjectIdField(primary_key=True)
    movement = EmbeddedDocumentListField(Classification)
    species = StringField()