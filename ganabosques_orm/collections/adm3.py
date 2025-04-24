from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Adm3(Document):
    """Auto-generated MongoDB collection: Adm3"""
    meta = {'collection': 'adm3'}
    id = ObjectIdField(primary_key=True)
    adm2_id = ObjectIdField(primary_key=True)
    name = StringField()
    ext_id = StringField()
    log = EmbeddedDocumentField(Log)