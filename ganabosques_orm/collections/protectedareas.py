from mongoengine import Document, StringField, ObjectIdField, EmbeddedDocumentField
from ganabosques_orm.auxiliaries.log import Log

class ProtectedAreas(Document):
    """Auto-generated MongoDB collection: ProtectedAreas"""
    meta = {'collection': 'protectedareas'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    path = StringField()
    log = EmbeddedDocumentField(Log)