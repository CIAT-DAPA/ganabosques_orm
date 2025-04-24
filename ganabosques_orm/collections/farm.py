from mongoengine import Document, ObjectIdField, EmbeddedDocumentField, EmbeddedDocumentListField, EnumField, ReferenceField
from ganabosques_orm.enums.farmsource import FarmSource
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.extidfarm import ExtIdFarm
from ganabosques_orm.collections.adm3 import Adm3

class Farm(Document):
    """Auto-generated MongoDB collection: Farm"""
    meta = {'collection': 'farm'}
    id = ObjectIdField(primary_key=True)
    adm3_id = ReferenceField(Adm3)
    ext_id = EmbeddedDocumentListField(ExtIdFarm)
    farm_source = EnumField(FarmSource)
    log = EmbeddedDocumentField(Log)