from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class ProtectedAreas(Document):
    """Auto-generated MongoDB collection: ProtectedAreas"""
    meta = {'collection': 'protectedareas'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    path = StringField()
    log = EmbeddedDocumentField(Log)