from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Adm2(Document):
    """Auto-generated MongoDB collection: Adm2"""
    meta = {'collection': 'adm2'}
    id = ObjectIdField(primary_key=True)
    adm1_id = ObjectIdField(primary_key=True)
    name = StringField()
    ext_id = StringField()
    log = EmbeddedDocumentField(Log)