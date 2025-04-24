from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Deforestation(Document):
    """Auto-generated MongoDB collection: Deforestation"""
    meta = {'collection': 'deforestation'}
    id = ObjectIdField(primary_key=True)
    deforestation_source = StringField()
    deforestation_type = StringField()
    name = StringField()
    year_start = StringField()
    year_end = StringField()
    path = StringField()
    log = EmbeddedDocumentField(Log)