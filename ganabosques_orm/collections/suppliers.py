from mongoengine import Document, EmbeddedDocumentField, ObjectIdField, ReferenceField
from ganabosques_orm.collections.farm import Farm
from ganabosques_orm.collections.enterprise import Enterprise
from ganabosques_orm.auxiliaries.log import Log



class Suppliers(Document):
    """Auto-generated MongoDB collection: Suppliers"""
    meta = {'collection': 'suppliers'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ReferenceField(Enterprise)
    farm_id = ReferenceField(Farm)
    log = EmbeddedDocumentField(Log)