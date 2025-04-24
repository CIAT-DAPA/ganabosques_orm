from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Configuration(Document):
    """Auto-generated MongoDB collection: Configuration"""
    meta = {'collection': 'configuration'}
    id = ObjectIdField(primary_key=True)
    parameters = StringField()
    log = EmbeddedDocumentField(Log)
    id = ObjectIdField(primary_key=True)
    parameters = StringField()
    log = EmbeddedDocumentField(Log)