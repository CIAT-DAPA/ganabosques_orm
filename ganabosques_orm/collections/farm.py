from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField
from typing import Optional
from ganabosques_orm.enums.farmsource import FarmSource
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.extidfarm import ExtIdFarm

class Farm(Document):
    """Auto-generated MongoDB collection: Farm"""
    meta = {'collection': 'farm'}
    id = ObjectIdField(primary_key=True)
    adm3_id = ObjectIdField(primary_key=True)
    ext_id = EmbeddedDocumentListField(ExtIdFarm)
    farm_source = EnumField(FarmSource)
    log = EmbeddedDocumentField(Log)