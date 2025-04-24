from mongoengine import Document, StringField, ObjectIdField, DateTimeField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, ReferenceField
from ganabosques_orm.enums.typemovement import TypeMovement
from ganabosques_orm.auxiliaries.sourcemovement import SourceMovement
from ganabosques_orm.auxiliaries.classification import Classification
from ganabosques_orm.collections.farm import Farm
from ganabosques_orm.collections.enterprise import Enterprise

class Movement(Document):
    """Auto-generated MongoDB collection: Movement"""
    meta = {'collection': 'movement'}
    id = ObjectIdField(primary_key=True)
    date = DateTimeField()
    type_origin = EnumField(TypeMovement)
    type_destination = EnumField(TypeMovement)
    source = EmbeddedDocumentField(SourceMovement)
    ext_id = StringField()
    farm_id_origin = ReferenceField(Farm)
    farm_id_destination = ReferenceField(Farm)
    enterprise_id_origin = ReferenceField(Enterprise)
    enterprise_id_destination = ReferenceField(Enterprise)
    movement = EmbeddedDocumentListField(Classification)
    species = StringField()