from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Enterprise(Document):
    """Auto-generated MongoDB collection: Enterprise"""
    meta = {'collection': 'enterprise'}
    id = ObjectIdField(primary_key=True)
    adm2_id = ObjectIdField(primary_key=True)
    name = StringField()
    ext_id = StringField()
    type_enterprise = StringField()
    latitude = StringField()
    longitud = StringField()
    log = EmbeddedDocumentField(Log)