from mongoengine import Document, StringField, ObjectIdField, EmbeddedDocumentField
from ganabosques_orm.auxiliaries.log import Log

class FarmingAreas(Document):
    """Auto-generated MongoDB collection: FarmingAreas"""
    meta = {'collection': 'farmingareas'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    path = StringField()
    log = EmbeddedDocumentField(Log)