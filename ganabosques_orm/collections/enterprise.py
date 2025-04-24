from mongoengine import Document, StringField, ObjectIdField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, FloatField, ReferenceField
from ganabosques_orm.enums.typeenterprise import TypeEnterprise
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.extidenterprise import ExtIdEnterprise
from ganabosques_orm.collections.adm2 import Adm2

class Enterprise(Document):
    """Auto-generated MongoDB collection: Enterprise"""
    meta = {'collection': 'enterprise'}
    id = ObjectIdField(primary_key=True)
    adm2_id = ReferenceField(Adm2)
    name = StringField()
    ext_id = EmbeddedDocumentListField(ExtIdEnterprise)
    type_enterprise = EnumField(TypeEnterprise)
    latitude = FloatField()
    longitud = FloatField()
    log = EmbeddedDocumentField(Log)