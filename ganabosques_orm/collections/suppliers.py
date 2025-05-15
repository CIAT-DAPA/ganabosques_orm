from mongoengine import Document, StringField, ObjectIdField, ReferenceField,EmbeddedDocumentField, EmbeddedDocumentListField
from ganabosques_orm.collections.farm import Farm
from ganabosques_orm.collections.enterprise import Enterprise
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.years import Years



class Suppliers(Document):
    """Auto-generated MongoDB collection: Suppliers"""
    meta = {'collection': 'suppliers'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ReferenceField(Enterprise)
    farm_id = ReferenceField(Farm)
    years = EmbeddedDocumentListField(Years)
    log = EmbeddedDocumentField(Log)