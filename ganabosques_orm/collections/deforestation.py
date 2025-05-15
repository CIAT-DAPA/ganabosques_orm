from mongoengine import Document, StringField, ObjectIdField, EmbeddedDocumentField, EnumField, IntField
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.enums.deforestationtype import DeforestationType
from ganabosques_orm.enums.deforestationsource import DeforestationSource

class Deforestation(Document):
    """Auto-generated MongoDB collection: Deforestation"""
    meta = {'collection': 'deforestation'}
    deforestation_source = EnumField(DeforestationSource)
    deforestation_type = EnumField(DeforestationType)
    name = StringField()
    year_start = IntField()
    year_end = IntField()
    path = StringField()
    log = EmbeddedDocumentField(Log)