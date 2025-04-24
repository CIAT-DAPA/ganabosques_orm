from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class FarmingAreas(Document):
    """Auto-generated MongoDB collection: FarmingAreas"""
    meta = {'collection': 'farmingareas'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    path = StringField()
    log = EmbeddedDocumentField(Log)