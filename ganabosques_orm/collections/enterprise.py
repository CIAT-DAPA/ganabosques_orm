from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, FloatField
from typing import Optional
from ganabosques_orm.enums.typeenterprise import TypeEnterprise
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.extidenterprise import ExtIdEnterprise

class Enterprise(Document):
    """Auto-generated MongoDB collection: Enterprise"""
    meta = {'collection': 'enterprise'}
    id = ObjectIdField(primary_key=True)
    adm2_id = ObjectIdField(primary_key=True)
    name = StringField()
    ext_id = EmbeddedDocumentListField(ExtIdEnterprise)
    type_enterprise = EnumField(TypeEnterprise)
    latitude = FloatField()
    longitud = FloatField()
    log = EmbeddedDocumentField(Log)