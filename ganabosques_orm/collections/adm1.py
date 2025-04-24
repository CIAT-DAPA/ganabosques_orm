from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Adm1(Document):
    """Auto-generated MongoDB collection: Adm1"""
    meta = {'collection': 'adm1'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    ext_id = StringField()
    log = EmbeddedDocumentField(Log)