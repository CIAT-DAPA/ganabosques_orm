from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional
from ganabosques_orm.auxiliaries.log import Log

class Farm(Document):
    """Auto-generated MongoDB collection: Farm"""
    meta = {'collection': 'farm'}
    id = ObjectIdField(primary_key=True)
    adm3_id = ObjectIdField(primary_key=True)
    ext_id = StringField()
    farm_source = StringField()
    log = EmbeddedDocumentField(Log)